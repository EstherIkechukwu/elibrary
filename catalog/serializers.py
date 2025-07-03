from rest_framework import serializers

from .models import Book, Author, BookImage


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email', 'dob']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)
    images = serializers.HyperlinkedRelatedField(
        view_name='book-images-detail',
        queryset=BookImage.objects.all(),
    )
    # images = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'summary','images','author']


class AddBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','isbn', 'summary']

class BookImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        book_id = self.context['id']
        return BookImage.objects.create(book_id=book_id, **validated_data)

    class Meta:
        model = BookImage
        fields = ['id', 'image']

