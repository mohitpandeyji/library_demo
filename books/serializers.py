from rest_framework import serializers

from books.models import Book, BookRating, Author, Genre, Language


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ["name"]


class BookSerializer(serializers.ModelSerializer):
    prefetch_related_fields = ["authors", "genre"]

    authors = AuthorSerializer(many=True)
    genre = GenreSerializer(many=True)
    language = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = "__all__"


class BookUpdateDeserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['price', 'description', 'genre']


class BookRatingSerializer(serializers.ModelSerializer):
    rating = serializers.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        model = Book
        fields = ['title', 'rating']


class BookRatingDeserializer(serializers.ModelSerializer):
    class Meta:
        model = BookRating
        fields = "__all__"
