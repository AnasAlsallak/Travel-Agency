from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Book
from django.contrib.auth import get_user_model


class BookTests(TestCase):
    def test_list_page_status_code(self):
        url = reverse("book_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("book_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "book/book-list.html")
        self.assertTemplateUsed(response, "_base.html")

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", email="teas@email.com", password="1234"
        )

        self.book = Book.objects.create(
            destination="test", desc="test info", agent=self.user,img_url="url"
        )

    def test_str_method(self):
        self.assertEqual(str(self.book), "test")

    def test_detail_view(self):
        url = reverse("book_detail", args=[self.book.pk])
        response = self.client.get(url)
        self.assertTemplateUsed(response, "book/book-detail.html")

    def test_create_view(self):
        obj = {
            "destination": "test2",
            "desc": "info...",
            "img_url": "url",
            "agent": self.user.pk,
        }

        url = reverse("book_create")
        response = self.client.post(path=url, data=obj, follow=True)
        self.assertRedirects(response, reverse("book_detail", args=[2]))