from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)
from rest_framework.response import Response

from .models import Book
from .serializers import (
    BookListSerializer,
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
