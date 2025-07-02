from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_books),

    path("authors/", views.AddAuthorView.as_view(), name="add_author"),

    path("authors/<int:pk>/", views.GetUpdateDeleteAuthorView.as_view(), name="update_author"),

    path("get/authors/", views.get_authors, name="get_authors"),

    path("greet/<name>", views.greet),
]