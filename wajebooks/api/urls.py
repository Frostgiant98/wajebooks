from django.urls import path
from . import views

urlpatterns = [

    path('', views.apiOverview, name='api-overview'),
	
    path('books/', views.bookList, name="book-list"), #GET book list
    path('book/<str:pk>/', views.book_Detail_Update, name="book-detailupdate"), # PUT update details and GET detail view
	
    path('authors/', views.authorList, name="author-list"), #GET book list
    path('author/<str:pk>/', views.author_Detail_Update, name="author-detailupdate"), # PUT update details and GET detail view

    path('author/', views.authorCreate, name="author-create"), #POST new book
    path('book/', views.bookCreate, name="book-create"), #POST new book

]