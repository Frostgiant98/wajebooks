
# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AuthorSerializer, BookSerializer

from .models import Book, Author

# Create your views here.

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
		'Book List':'/books/',
		'Book Detail':'/books/<str:pk>/',

		'Author List':'/authors/',
		'Author Detail ':'/author/<str:pk>/',

		'Create Author':'/author/',
		'Create Book':'/book/',

		'Update Author':'/author/<str:pk>/',
		'Update Author':'/book/<str:pk>/',
		}
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Book.objects.all().order_by('-id')
	serializer = BookSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Book.objects.get(id=pk)
	serializer = BookSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = BookSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def taskUpdate(request, pk):
	task = Book.objects.get(id=pk)
	serializer = BookSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

