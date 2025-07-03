from rest_framework import serializers

from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'summary', 'author']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']

class AddBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','isbn', 'summary']