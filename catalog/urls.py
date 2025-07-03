from django.urls import path, include
from . import views
from rest_framework_nested import routers
# from rest_framework import routers

from .views import BookViewSet, BookImageViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='books')

router.register('images', BookImageViewSet, basename='book-images')

book_image_router = routers.NestedDefaultRouter(router, 'books', lookup='book')
book_image_router.register('images', BookImageViewSet, basename='book-images')

urlpatterns = [

    path('', include(router.urls)),

    path('', include(book_image_router.urls)),
    path("", views.get_books),

    path("authors/", views.AddAuthorView.as_view(), name="add_author"),

    path("authors/<int:pk>/", views.GetUpdateDeleteAuthorView.as_view()),

    path("image/<int:pk>/", views.image_detail, name="book-images-detail"),

    # path("update/authors/<int:pk>", views.update_author, name="update_author"),
    # path("delete/authors/<int:pk>", views.delete_author, name="delete_author"),
    path("get/authors/", views.get_authors, name="get_authors"),

    path("greet/<name>", views.greet),


]