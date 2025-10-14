from django.contrib import admin
from .models import Author, Book, Member, BorrowRecord

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date')
    search_fields = ('first_name', 'last_name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'pages', 'available')
    list_filter = ('available', 'author')
    search_fields = ('title', 'isbn')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'membership_date', 'is_active', 'role')
    list_filter = ('is_active', 'role')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'borrow_date', 'return_date', 'is_returned')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('book__title', 'member__user__username')
    
    def is_returned(self, obj):
        return obj.return_date is not None
    is_returned.boolean = True
    is_returned.short_description = 'Devolvido'