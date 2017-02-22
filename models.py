from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, models.CASCADE, related_name="books")
    title = models.CharField(max_length=150)

    def __str__(self):
        return "%s by %s" % (self.title, self.author)
