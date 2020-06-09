from django.db import models
from django.db.models import SET_NULL

from library_api.models.model_mixins import LibraryBaseModel, Timestampable
from users.models import User


class Genre(LibraryBaseModel):
    name = models.CharField(max_length=200, help_text="Enter a book genre")

    def __str__(self):
        return self.name


class Language(LibraryBaseModel):
    name = models.CharField(max_length=200, help_text="Enter a book language")

    def __str__(self):
        return self.name


class Author(Timestampable):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f" {self.first_name} - {self.last_name} "


class Book(Timestampable):
    isbn = models.CharField(max_length=32)
    title = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author, related_name='book_auths')
    genre = models.ManyToManyField(Genre, help_text="Selct a genre for this book")
    language = models.OneToOneField(Language, on_delete=SET_NULL, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pub_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class BookRating(Timestampable):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(choices=[(i, i) for i in range(1, 6)], default=1)

    def __str__(self):
        return f"{self.user}"
