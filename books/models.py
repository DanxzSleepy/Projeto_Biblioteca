from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['last_name']

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    pages = models.IntegerField()
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    class Meta:
        ordering = ['title']

class Member(models.Model):
    USER_ROLE_CHOICES = [
        ('member', 'Membro'),
        ('librarian', 'Bibliotecário'),
        ('admin', 'Administrador'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    membership_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES, default='member')
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.get_role_display()})"
    
    @property
    def is_librarian(self):
        return self.role == 'librarian' or self.role == 'admin'
    
    @property
    def is_admin(self):
        return self.role == 'admin'

class BookRequest(models.Model):
    REQUEST_STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('approved', 'Aprovado'),
        ('rejected', 'Rejeitado'),
        ('completed', 'Concluído'),
    ]
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=REQUEST_STATUS_CHOICES, default='pending')
    approval_date = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_requests')
    rejection_reason = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.book.title} requested by {self.member.user.username}"
    
    class Meta:
        ordering = ['-request_date']

class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.book.title} borrowed by {self.member.user.username}"
    
    @property
    def is_returned(self):
        return self.return_date is not None