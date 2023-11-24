from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from book.models import Book
from book.serializers import BookSerializer


# Create your views here.
class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookRetrieveAPIView(RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookCreateAPIView(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookUpdateAPIView(UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDestroyAPIView(DestroyAPIView):
    queryset = Book.objects.all()
