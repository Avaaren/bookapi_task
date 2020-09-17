from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListView.as_view()),
    # path('<int:book_id>', views.BookDetailView.as_view()),
]