from django.contrib import admin

from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    class Meta:
        list_display = '__all__'