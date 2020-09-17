from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
)
from rest_framework.response import Response

from .models import Book
from .serializers import (
    BookListSerializer,
    BookDetailSerializer,
)


class BookListView(ListAPIView):
    '''Отображение списка книг'''
    queryset = Book.objects.all()
    serializer_class = BookListSerializer

    def get(self, request):
        '''Отображение списка всех книг'''
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)


class BookDetailView(RetrieveAPIView):
    '''Получение информации о книге'''
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

    def get_object(self):
        pk = self.kwargs.get('book_id')
        return get_object_or_404(Book, pk=pk)


class BookCreateView(CreateAPIView):
    '''Добавление новой книги'''
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

    