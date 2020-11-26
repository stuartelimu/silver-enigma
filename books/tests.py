from django.test import TestCase, SimpleTestCase
from django.urls import reverse

from .models import Book


class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_page_view_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_home_page_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')


class BookTests(TestCase):
    
    def setUp(self):
        Book.objects.create(title='Hello, world!', author='Admin')

    def test_book_str(self):
        book = Book.objects.create(title='Hello, world!', author='Admin')
        self.assertEquals(str(book), 'Hello, world!')

    def test_book_creation(self):
        book = Book.objects.get(id=1)
        self.assertTrue(isinstance(book, Book))
        self.assertEquals(str(book), 'Hello, world!')

    def test_book_list_view_status_code(self):
        response = self.client.get(reverse('book_list'))
        self.assertEquals(response.status_code, 200)

    def test_book_list_view_uses_correct_template(self):
        response = self.client.get(reverse('book_list'))
        self.assertTemplateUsed(response, 'book_list.html')

    def test_book_detail_view_success_status_code(self):
        book = Book.objects.create(title='Hello, world!', author='Admin')
        response = self.client.get(reverse('book_detail', kwargs={'pk':book.id}))
        self.assertEquals(response.status_code, 200)

    def test_book_detail_view_not_found_status_code(self):
        response = self.client.get(reverse('book_detail', kwargs={'pk':99}))
        self.assertEquals(response.status_code, 404)

    
