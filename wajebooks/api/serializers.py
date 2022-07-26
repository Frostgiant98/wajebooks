from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Author
        fields = ['author_id','first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(many = False, read_only = True)

    class Meta:
        model =  Book
        fields = ['name', 'isbn', 'author']