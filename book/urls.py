from django.urls import path

from book.apps import BookConfig
from book.views import *

app_name = BookConfig.name

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book_list'),
    path('<int:pk>', BookRetrieveAPIView.as_view(), name='book_detail'),
    path('create', BookCreateAPIView.as_view(), name='book_create'),
    path('update/<int:pk>', BookUpdateAPIView.as_view(), name='book_update'),
    path('destroy/<int:pk>', BookDestroyAPIView.as_view(), name='book_destroy'),
]
