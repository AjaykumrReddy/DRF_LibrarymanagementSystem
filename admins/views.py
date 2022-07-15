from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LibrarySerializer
from .models import Library

# Create your views here.


@api_view(['POST'])
def add_books(request):
    serializer = LibrarySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def view_books(request):
    books = Library.objects.all()
    serializer = LibrarySerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def update_book(request, pk):
    book = Library.objects.get(id=pk)
    serializer = LibrarySerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def delete_book(request, pk):
    book = Library.objects.get(id=pk)
    book.delete()
    return Response("Book deleted successfully.")
