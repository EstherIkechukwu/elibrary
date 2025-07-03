from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from catalog.models import Book
from catalog.serializers import BookSerializer, AuthorSerializer, AddBookSerializer
from .models import Author


# Create your views here.

def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#
# @api_view(['POST'])
# def add_author(request):
#     author = AuthorSerializer(data=request.data)
#     author.is_valid(raise_exception=True)
#     author.save()
#     return Response(author.data, status=status.HTTP_201_CREATED)

class AddAuthorView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GetUpdateDeleteAuthorView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return AddBookSerializer
        elif self.request.method == 'POST':
            return AddBookSerializer
        return BookSerializer


@api_view(['GET'])
def get_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['PUT', 'PATCH'])
# def update_author(request, id):
#     author = Author.objects.get(pk=id)
#     serializer = AuthorSerializer(author, data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['DELETE'])
# def delete_author(request, pk):
#     author = Author.objects.get(pk=pk)
#     author.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

def greet(request, name):
    return render(request, 'index.html', context={'name': name})