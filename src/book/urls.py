from django.urls import path

from src.book.apps import BookConfig
from src.book.views import *

app_name = BookConfig.name

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book_list'),
    path('<int:pk>', BookRetrieveAPIView.as_view(), name='book_detail'),
    path('create', BookCreateAPIView.as_view(), name='book_create'),
    path('update/<int:pk>', BookUpdateAPIView.as_view(), name='book_update'),
    path('delete/<int:pk>', BookDestroyAPIView.as_view(), name='book_delete'),
]
