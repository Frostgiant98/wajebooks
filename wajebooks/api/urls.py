from django.urls import path
from . import views

urlpatterns = [

    path('', views.apiOverview, name='api-overview'),
	path('books/', views.bookList, name="book-list"), #GET book list
    path('book/', views.bookCreate, name="book-create"), #POST new book
    path('book/<str:pk>/', views.bookDetail, name="book-detail"), #GET datail
    path('book/<str:pk>/', views.bookUpdate, name="book-update"), #PUT book update


]