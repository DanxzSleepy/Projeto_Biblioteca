from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import logout
from .models import Book, Author, Member, BorrowRecord
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
def borrow_book(request, book_id):
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
    
    # Create borrow record
    BorrowRecord.objects.create(
        book=book,
        member=member,
        borrow_date=date.today()
    )
    
    # Mark book as unavailable
    book.available = False
    book.save()
    
    messages.success(request, f'Empréstimo do livro "{book.title}" solicitado com sucesso!')
    return HttpResponseRedirect(reverse('book_list'))

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
    
    messages.success(request, f'Livro "{borrow_record.book.title}" devolvido com sucesso!')
    return HttpResponseRedirect(reverse('borrow_list'))

def profile_view(request):
    """View user profile"""
    if request.user.is_authenticated:
        try:
            member = request.user.member
        except Member.DoesNotExist:
            # Create a member profile if it doesn't exist
            member = Member.objects.create(
                user=request.user,
                phone_number="",
                role='member'
            )
        return render(request, 'books/profile.html', {'member': member})
    else:
        return HttpResponseRedirect(reverse('login'))

def logout_view(request):
    """Custom logout view"""
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return HttpResponseRedirect(reverse('index'))