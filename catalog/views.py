from django.core.mail import send_mail
from django.core.serializers import serialize
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from catalog.models import Book, BookImage, BookInstance
from catalog.serializers import BookSerializer, AuthorSerializer, AddBookSerializer, BookImageSerializer, \
    BookInstanceSerializer
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

@api_view(['GET'])
def get_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class AddAuthorView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GetUpdateDeleteAuthorView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

def greet(request, name):
    return render(request, 'index.html', context={'name': name})

@api_view(['GET'])
def image_detail(request, pk):
    book_image = get_object_or_404(BookImage, pk=pk)
    serializer = BookImageSerializer(book_image)
    return Response(serializer.data, status=status.HTTP_200_OK)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return AddBookSerializer
        elif self.request.method == 'POST':
            return AddBookSerializer
        return BookSerializer

class BookImageViewSet(viewsets.ModelViewSet):
    queryset = BookImage.objects.all()
    serializer_class = BookImageSerializer

    def perform_create(self, serializer):
        print("KWARGS IN PERFORM CREATE: ", self.kwargs)
        book_id = self.kwargs.get("book_pk")
        if not book_id:
            raise ValueError("book_id missing in kwargs!")
        serializer.save(book_id=book_id)

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def borrow_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user = request.user
    data = BookInstanceSerializer(data=request.data)
    data.is_valid(raise_exception=True)
    BookInstance.objects.create(
        user=user,
        book=book,
        comments= data.validated_data['comments'],
        return_date=data.validated_data['return_date'],
    )
    subject = "Notification from ELibrary"
    message = f"""
                    The request to borrow book  {book.title} is successful, you can pick from the admin desk"""
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['user.email']
    send_mail(subject=subject,
              message=message,
              from_email=from_email,
              recipient_list=recipient_list)
    return Response({"message": "book borrowed successfully"}, status=status.HTTP_200_OK)


    # book = get_object_or_404(Book, pk=pk)
    # user = request.user
    # data = BookInstanceSerializer(data=request.data)
    # data.is_valid(raise_exception=True)
    # book_instance = BookInstance()
    # book_instance.user = user
    # book_instance.book = book
    # book_instance.return_date = data.validated_data['return_date']
    # book_instance.comments = data.validated_data['comments']
    # book_instance.save()
    # return Response({"message": "book borrowed successfully"}, status=status.HTTP_200_OK)

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

