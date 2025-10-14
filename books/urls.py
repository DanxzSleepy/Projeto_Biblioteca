from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('authors/', views.author_list, name='author_list'),
    path('members/', views.member_list, name='member_list'),
    path('borrows/', views.borrow_list, name='borrow_list'),
    path('requests/', views.request_list, name='request_list'),
    path('books/<int:book_id>/request/', views.request_book, name='request_book'),
    path('requests/<int:request_id>/approve/', views.approve_request, name='approve_request'),
    path('requests/<int:request_id>/reject/', views.reject_request, name='reject_request'),
    path('borrows/<int:borrow_id>/return/', views.return_book, name='return_book'),
    path('profile/', views.profile_view, name='profile'),
    path('accounts/logout/', views.logout_view, name='logout'),
]