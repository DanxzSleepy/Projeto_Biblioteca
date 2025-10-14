from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('authors/', views.author_list, name='author_list'),
    path('members/', views.member_list, name='member_list'),
    path('borrows/', views.borrow_list, name='borrow_list'),
]