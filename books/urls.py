from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('authors/', views.author_list, name='author_list'),
    path('members/', views.member_list, name='member_list'),
    path('borrows/', views.borrow_list, name='borrow_list'),
    path('books/<int:book_id>/borrow/', views.borrow_book, name='borrow_book'),
    path('borrows/<int:borrow_id>/return/', views.return_book, name='return_book'),
    path('profile/', views.profile_view, name='profile'),
]