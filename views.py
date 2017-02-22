from django.views import generic
from django.urls import reverse

from .models import Author, Book


class Authors(generic.ListView):
    model = Author


class Books(generic.ListView):
    model = Book

    def get_queryset(self):
        return Author.objects.get(pk=self.kwargs["pk"]).books.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = Author.objects.get(pk=self.kwargs["pk"])
        return context

class BookDelete(generic.edit.DeleteView):
    model = Book

    def get_success_url(self):
        book = self.get_object()
        return reverse("author:books", args=(book.author.pk,))

class BookCreate(generic.edit.UpdateView):
    model = Book
    fields = ["title"]

    def get_success_url(self):
        return reverse("author:books", args=(self.kwargs["pk"],))

    def get_object(self):
        return Book(author=Author.objects.get(pk=self.kwargs["pk"]))

class BookUpdate(generic.edit.UpdateView):
    model = Book
    fields = ["title"]

    def get_success_url(self):
        book = self.get_object()
        return reverse("author:books", args=(book.author.pk,))
