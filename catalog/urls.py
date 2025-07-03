from django.urls import path, include
from . import views
from rest_framework import routers

from .views import BookViewSet, BookImageViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='books')

router.register('images', BookImageViewSet, basename='images')

print(router.urls)

urlpatterns = [

    path('', include(router.urls)),
    path("", views.get_books),

    path("authors/", views.AddAuthorView.as_view(), name="add_author"),

    path("authors/<int:pk>/", views.GetUpdateDeleteAuthorView.as_view(), name="update_author"),

    path("get/authors/", views.get_authors, name="get_authors"),

    path("greet/<name>", views.greet),

    path("image/<int:pk>/", views.image_detail.as_view(), name="image-detail"),
]