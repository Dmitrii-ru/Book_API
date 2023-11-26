from django.urls import path

from book.views import (
    BooksAllAPIView,
    BookAPIView,
    BookCreateAPIView,
    BookUpdateAPIView,
    BookDeleteAPIView,
    CreateUserView
)

app_name = 'book'
urlpatterns = [
    path('books/', BooksAllAPIView.as_view({'get': 'list'}), name='books'),
    path('book/<int:id>', BookAPIView.as_view(), name='book-get'),
    path('book/create', BookCreateAPIView.as_view(), name='book-crete'),
    path('book/update/<int:id>', BookUpdateAPIView.as_view(), name='book-update'),
    path('book/delete/<int:id>', BookDeleteAPIView.as_view(), name='book-delete'),
    path('user/create', CreateUserView.as_view(), name='user-create')
]