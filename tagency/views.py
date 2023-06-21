from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Book

from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "home.html"


class BookListView(ListView):
    template_name = "book/book-list.html"
    model = Book


class BookDetailView(DetailView):
    template_name = "book/book-detail.html"
    model = Book


class BookCreateView(CreateView):
    template_name = "book/book-create.html"
    model = Book
    fields = ['destination','agent','desc','img_url']


class BookUpdateView(UpdateView):
    template_name = "book/book-update.html"
    model = Book
    fields = ['destination','agent','desc','img_url']


class BookDeleteView(DeleteView):
    template_name = "book/book-delete.html"
    model = Book
    success_url = reverse_lazy("book_list")