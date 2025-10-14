from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Book, Author, Member, BorrowRecord

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

def book_list(request):
    """Display all books"""
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def author_list(request):
    """Display all authors"""
    authors = Author.objects.all()
    return render(request, 'books/author_list.html', {'authors': authors})

def member_list(request):
    """Display all members"""
    members = Member.objects.all()
    return render(request, 'books/member_list.html', {'members': members})

def borrow_list(request):
    """Display all borrow records"""
    borrows = BorrowRecord.objects.all()
    return render(request, 'books/borrow_list.html', {'borrows': borrows})