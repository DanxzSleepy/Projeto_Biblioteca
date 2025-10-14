from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    
    # Intentional error: Missing __str__ method
    # This will cause issues when displaying authors in admin or forms
    
    class Meta:
        # Intentional error: Incorrect ordering field name
        ordering = ['lastname']  # Should be 'last_name'

class Book(models.Model):
    title = models.CharField(max_length=200)
    # Intentional error: Forgetting to add related_name
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    # Intentional error: Incorrect field type for pages (should be IntegerField)
    pages = models.CharField(max_length=10)
    available = models.BooleanField(default=True)
    
    # Intentional error: Incorrect reference to author field in __str__
    def __str__(self):
        return f"{self.title} by {self.authors.name}"  # Should be self.author
    
    class Meta:
        # Intentional error: Incorrect ordering field
        ordering = ['book_title']  # Should be 'title'

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Intentional error: Missing max_length for CharField
    phone_number = models.CharField()
    membership_date = models.DateField(auto_now_add=True)
    # Intentional error: Incorrect default value type (should be boolean)
    is_active = models.BooleanField(default="True")
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    # Intentional error: Incorrect field name in __str__
    def __str__(self):
        return f"{self.book.title} borrowed by {self.member.users.username}"  # Should be self.member.user.username