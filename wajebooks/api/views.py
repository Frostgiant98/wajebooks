
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
def bookList(request):
	tasks = Book.objects.all().order_by('book_id')
	serializer = BookSerializer(tasks, many=True)
	# return JsonResponse(serializer.data, safe=False)
	return Response(serializer.data)


@api_view(['GET'])
def authorList(request):
	tasks = Author.objects.all().order_by('author_id')
	serializer = AuthorSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def authorDetail(request, pk):
	tasks = Author.objects.get(author_id=pk)
	serializer = AuthorSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def bookCreate(request):
	serializer = BookSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def authorCreate(request):
	serializer = AuthorSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['GET','PUT'])
def book_Detail_Update(request,pk):
    if request.method == "PUT":
        task = Book.objects.get(book_id=pk)
        serializer = BookSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == "GET":
        tasks = Book.objects.get(book_id=pk)
        serializer = BookSerializer(tasks, many=False)
        return Response(serializer.data)
    else:
        return JsonResponse('Invalid Response', safe=False)

@api_view(['GET','PUT'])
def author_Detail_Update(request,pk):
    if request.method == "PUT":
        task = Author.objects.get(author_id=pk)
        serializer = AuthorSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == "GET":
        tasks = Author.objects.get(author_id=pk)
        serializer = AuthorSerializer(tasks, many=False)
        return Response(serializer.data)
    else:
        return JsonResponse('Invalid Response', safe=False)


@api_view(['PUT'])
def authorUpdate(request, pk):
	task = Author.objects.get(author_id=pk)
	serializer = AuthorSerializer(instance=task, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


