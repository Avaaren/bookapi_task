from django.db import models


class Book(models.Model):
    title = models.CharField("Название книги", max_length=35)
    author_name = models.CharField("Имя автора", max_length=50)

    def __str__(self):
        return f"{self.title} by {self.author_name}"

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
