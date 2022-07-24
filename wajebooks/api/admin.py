from django.contrib import admin

from api.models import Book, Author

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)