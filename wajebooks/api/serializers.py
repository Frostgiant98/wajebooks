from rest_framework import serializers
from .models import Task

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Task
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Task
        fields = '__all__'