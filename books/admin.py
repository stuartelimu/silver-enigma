from django.contrib import admin
from .models import Book

admin.sites.register(Book)