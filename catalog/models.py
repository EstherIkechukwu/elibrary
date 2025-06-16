import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Author(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     dob = models.DateField()
#     email = models.EmailField()

class Language(models.Model):
    LANGUAGES = (
        ('en', 'English'),
        ('fr', 'French'),
        ('i', 'Igbo'),
        ('y', 'Yoruba'),
        ('h', 'Hausa')
    )
    name = models.CharField(max_length=3, choices=LANGUAGES, default='en')

    def __str__(self):
        return self.name

class Genre(models.Model):
    GENRE_CHOICES = (
        ("R", "ROMANCE"),
        ("C", "COMEDY"),
        ("P", "POLITICS"),
        ("F", "FINANCE"),
    )
    name = models.CharField(max_length=1, choices=GENRE_CHOICES, default="F")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = ""
    summary = models.TextField()
    isbn = models.CharField(max_length=11, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class BookInstance(models.Model):
    LOAN_STATUS = (
        ("A", "AVAILABLE"),
        ("B", "BORROWED"),
        ("M", "MAINTENANCE"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default="A")
    return_date = models.DateTimeField(blank=False, null=False)
    comments = models.TextField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

