from django.urls import path
from . import views

urlpatterns = [

    path('', views.apiOverview, name='api-overview'),
    path('book/<str:pk>/', views.book_Detail_Update, name="book-detailupdate"), # PUT update details and GET detail view
	path('books/', views.bookList, name="book-list"), #GET book list
    path('book/', views.bookCreate, name="book-create"), #POST new book


]