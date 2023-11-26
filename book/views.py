from book.models import Book
from .serializers import BookSerializer, CustomUserCreateSerializer
from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Book
from rest_framework import generics, status


class BooksAllAPIView(ReadOnlyModelViewSet):
    """
    Get all books
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def list(self, request, *args, **kwargs):
        data = self.get_serializer(self.get_queryset(), many=True).data
        return Response(data, status=status.HTTP_200_OK)


class BookAPIView(generics.RetrieveAPIView):
    """
    Get single book
    params: id
    """
    lookup_field = 'id'
    serializer_class = BookSerializer
    queryset = Book.objects.all()



class BookCreateAPIView(generics.CreateAPIView):
    """
    Create book
    """
    serializer_class = BookSerializer


class BookUpdateAPIView(UpdateAPIView):
    """
    Update book
    params: id
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()



class BookDeleteAPIView(DestroyAPIView):
    """
    Delete book
    params: id
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()



class CreateUserView(generics.CreateAPIView):
    """
    Create user
    """
    serializer_class = CustomUserCreateSerializer
