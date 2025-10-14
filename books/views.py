from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Author, Member, BorrowRecord, BookRequest
from django.contrib.auth.models import User
from datetime import date

def index(request):
    """Home page showing library statistics"""
    total_books = Book.objects.count()
    total_authors = Author.objects.count()
    total_members = Member.objects.count()
    borrowed_books = BorrowRecord.objects.filter(return_date__isnull=True).count()
    
    context = {
        'total_books': total_books,
        'total_authors': total_authors,
        'total_members': total_members,
        'borrowed_books': borrowed_books,
    }
    return render(request, 'books/index.html', context)

@login_required
def book_list(request):
    """Display all books"""
    books = Book.objects.all()
    # Check if user has a member profile
    try:
        member = request.user.member
        is_librarian = member.is_librarian
    except Member.DoesNotExist:
        is_librarian = False
    
    return render(request, 'books/book_list.html', {
        'books': books,
        'is_librarian': is_librarian
    })

@login_required
def author_list(request):
    """Display all authors"""
    authors = Author.objects.all()
    # Check if user has a member profile
    try:
        member = request.user.member
        is_librarian = member.is_librarian
    except Member.DoesNotExist:
        is_librarian = False
    
    return render(request, 'books/author_list.html', {
        'authors': authors,
        'is_librarian': is_librarian
    })

@login_required
def member_list(request):
    """Display all members - only accessible to librarians and admins"""
    try:
        member = request.user.member
        if not member.is_librarian:
            messages.error(request, 'Acesso negado. Apenas bibliotecários e administradores podem acessar esta página.')
            return HttpResponseRedirect(reverse('index'))
    except Member.DoesNotExist:
        messages.error(request, 'Acesso negado. Apenas bibliotecários e administradores podem acessar esta página.')
        return HttpResponseRedirect(reverse('index'))
    
    members = Member.objects.all()
    return render(request, 'books/member_list.html', {'members': members})

@login_required
def borrow_list(request):
    """Display all borrow records - only accessible to librarians and admins"""
    try:
        member = request.user.member
        if not member.is_librarian:
            messages.error(request, 'Acesso negado. Apenas bibliotecários e administradores podem acessar esta página.')
            return HttpResponseRedirect(reverse('index'))
    except Member.DoesNotExist:
        messages.error(request, 'Acesso negado. Apenas bibliotecários e administradores podem acessar esta página.')
        return HttpResponseRedirect(reverse('index'))
    
    borrows = BorrowRecord.objects.all()
    return render(request, 'books/borrow_list.html', {'borrows': borrows})

@login_required
def user_dashboard(request):
    """Display user dashboard with borrowed books and requests"""
    try:
        member = request.user.member
    except Member.DoesNotExist:
        messages.error(request, 'Você precisa ter um perfil de membro para acessar o painel.')
        return HttpResponseRedirect(reverse('index'))
    
    # Get borrowed books (not returned yet) for the current user only
    borrowed_books = BorrowRecord.objects.filter(
        member=member, 
        return_date__isnull=True
    ).select_related('book')
    
    # Calculate overdue books
    today = date.today()
    for record in borrowed_books:
        # Assuming 14 days loan period
        due_date = record.borrow_date + timezone.timedelta(days=14)
        if today > due_date:
            record.is_overdue = True
            record.days_overdue = (today - due_date).days
        else:
            record.is_overdue = False
    
    # Get user's book requests
    book_requests = BookRequest.objects.filter(member=member).select_related('book')
    
    context = {
        'member': member,
        'borrowed_books': borrowed_books,
        'book_requests': book_requests,
        'today': today,
    }
    
    return render(request, 'books/user_dashboard.html', context)

@login_required
def request_book(request, book_id):
    """Allow members to request to borrow a book"""
    book = get_object_or_404(Book, id=book_id)
    
    # Check if user has a member profile
    try:
        member = request.user.member
    except Member.DoesNotExist:
        messages.error(request, 'Você precisa ter um perfil de membro para solicitar empréstimos.')
        return HttpResponseRedirect(reverse('book_list'))
    
    # Check if book is available
    if not book.available:
        messages.error(request, 'Este livro não está disponível para empréstimo.')
        return HttpResponseRedirect(reverse('book_list'))
    
    # Check if user already has a pending request for this book
    existing_request = BookRequest.objects.filter(
        book=book, 
        member=member, 
        status__in=['pending', 'approved']
    ).first()
    
    if existing_request:
        messages.error(request, 'Você já possui uma solicitação pendente ou aprovada para este livro.')
        return HttpResponseRedirect(reverse('book_list'))
    
    # Create book request
    BookRequest.objects.create(
        book=book,
        member=member
    )
    
    messages.success(request, f'Solicitação de empréstimo do livro "{book.title}" enviada com sucesso! Aguarde a aprovação do bibliotecário.')
    return HttpResponseRedirect(reverse('book_list'))

@login_required
def request_list(request):
    """Display book requests - members see their requests, librarians see all requests"""
    try:
        member = request.user.member
    except Member.DoesNotExist:
        messages.error(request, 'Você precisa ter um perfil de membro para acessar esta página.')
        return HttpResponseRedirect(reverse('index'))
    
    if member.is_librarian:
        # Librarians see all requests
        requests = BookRequest.objects.all()
    else:
        # Members see only their own requests
        requests = BookRequest.objects.filter(member=member)
    
    return render(request, 'books/request_list.html', {'requests': requests})

@login_required
def approve_request(request, request_id):
    """Allow librarians to approve book requests"""
    # Check if user has a member profile and is a librarian
    try:
        member = request.user.member
        if not member.is_librarian:
            messages.error(request, 'Acesso negado. Apenas bibliotecários podem aprovar solicitações.')
            return HttpResponseRedirect(reverse('index'))
    except Member.DoesNotExist:
        messages.error(request, 'Acesso negado. Apenas bibliotecários podem aprovar solicitações.')
        return HttpResponseRedirect(reverse('index'))
    
    book_request = get_object_or_404(BookRequest, id=request_id)
    
    # Check if request is already processed
    if book_request.status != 'pending':
        messages.error(request, 'Esta solicitação já foi processada.')
        return HttpResponseRedirect(reverse('request_list'))
    
    # Check if book is still available
    if not book_request.book.available:
        messages.error(request, 'Este livro não está mais disponível para empréstimo.')
        book_request.status = 'rejected'
        book_request.rejection_reason = 'Livro não está mais disponível'
        book_request.save()
        return HttpResponseRedirect(reverse('request_list'))
    
    # Approve the request
    book_request.status = 'approved'
    book_request.approval_date = timezone.now()
    book_request.approved_by = member
    book_request.save()
    
    # Create borrow record
    BorrowRecord.objects.create(
        book=book_request.book,
        member=book_request.member,
        borrow_date=date.today()
    )
    
    # Mark book as unavailable
    book_request.book.available = False
    book_request.book.save()
    
    messages.success(request, f'Solicitação de "{book_request.book.title}" aprovada com sucesso!')
    return HttpResponseRedirect(reverse('request_list'))

@login_required
def reject_request(request, request_id):
    """Allow librarians to reject book requests"""
    # Check if user has a member profile and is a librarian
    try:
        member = request.user.member
        if not member.is_librarian:
            messages.error(request, 'Acesso negado. Apenas bibliotecários podem rejeitar solicitações.')
            return HttpResponseRedirect(reverse('index'))
    except Member.DoesNotExist:
        messages.error(request, 'Acesso negado. Apenas bibliotecários podem rejeitar solicitações.')
        return HttpResponseRedirect(reverse('index'))
    
    book_request = get_object_or_404(BookRequest, id=request_id)
    
    # Check if request is already processed
    if book_request.status != 'pending':
        messages.error(request, 'Esta solicitação já foi processada.')
        return HttpResponseRedirect(reverse('request_list'))
    
    # Reject the request
    if request.method == 'POST':
        reason = request.POST.get('rejection_reason', '')
        book_request.status = 'rejected'
        book_request.rejection_reason = reason
        book_request.approval_date = timezone.now()
        book_request.approved_by = member
        book_request.save()
        
        messages.success(request, f'Solicitação de "{book_request.book.title}" rejeitada.')
        return HttpResponseRedirect(reverse('request_list'))
    else:
        return render(request, 'books/reject_request.html', {'request': book_request})

@login_required
def return_book(request, borrow_id):
    """Allow librarians to process book returns"""
    # Check if user has a member profile and is a librarian
    try:
        member = request.user.member
        if not member.is_librarian:
            messages.error(request, 'Acesso negado. Apenas bibliotecários podem processar devoluções.')
            return HttpResponseRedirect(reverse('index'))
    except Member.DoesNotExist:
        messages.error(request, 'Acesso negado. Apenas bibliotecários podem processar devoluções.')
        return HttpResponseRedirect(reverse('index'))
    
    borrow_record = get_object_or_404(BorrowRecord, id=borrow_id)
    
    # Check if book is already returned
    if borrow_record.return_date:
        messages.error(request, 'Este livro já foi devolvido.')
        return HttpResponseRedirect(reverse('borrow_list'))
    
    # Process return
    borrow_record.return_date = date.today()
    borrow_record.save()
    
    # Mark book as available
    borrow_record.book.available = True
    borrow_record.book.save()
    
    # Update any approved requests for this book to completed
    BookRequest.objects.filter(
        book=borrow_record.book,
        status='approved'
    ).update(status='completed')
    
    messages.success(request, f'Livro "{borrow_record.book.title}" devolvido com sucesso!')
    return HttpResponseRedirect(reverse('borrow_list'))

@login_required
def return_book_user(request, borrow_id):
    """Allow users to return their borrowed books"""
    try:
        member = request.user.member
    except Member.DoesNotExist:
        messages.error(request, 'Você precisa ter um perfil de membro para devolver livros.')
        return HttpResponseRedirect(reverse('index'))
    
    # Get the borrow record and ensure it belongs to the current user
    borrow_record = get_object_or_404(BorrowRecord, id=borrow_id, member=member)
    
    # Check if book is already returned
    if borrow_record.return_date:
        messages.error(request, 'Este livro já foi devolvido.')
        return HttpResponseRedirect(reverse('user_dashboard'))
    
    # Process return
    borrow_record.return_date = date.today()
    borrow_record.save()
    
    # Mark book as available
    borrow_record.book.available = True
    borrow_record.book.save()
    
    # Update any approved requests for this book to completed
    BookRequest.objects.filter(
        book=borrow_record.book,
        status='approved'
    ).update(status='completed')
    
    messages.success(request, f'Livro "{borrow_record.book.title}" devolvido com sucesso!')
    return HttpResponseRedirect(reverse('user_dashboard'))

def profile_view(request):
    """View and edit user profile"""
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    try:
        member = request.user.member
    except Member.DoesNotExist:
        # Create a member profile if it doesn't exist
        member = Member.objects.create(
            user=request.user,
            phone_number="",
            role='member'
        )
    
    if request.method == 'POST':
        # Update user information
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phone_number', '')
        
        # Update User model
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.email = email
        request.user.save()
        
        # Update Member model
        member.phone_number = phone_number
        member.save()
        
        messages.success(request, 'Perfil atualizado com sucesso!')
        return HttpResponseRedirect(reverse('profile'))
    
    return render(request, 'books/profile.html', {'member': member})

def logout_view(request):
    """Custom logout view"""
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return HttpResponseRedirect(reverse('index'))

def register(request):
    """Handle user registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create member profile
            Member.objects.create(
                user=user,
                phone_number="",
                role='member'  # Default role is member
            )
            messages.success(request, 'Conta criada com sucesso! Você pode fazer login agora.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
