from django.contrib import admin

from books.models import Genre, Language, Author, BookRating, Book


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    show_full_result_count = False
    list_select_related = True


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    show_full_result_count = False
    list_select_related = True


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name"]
    show_full_result_count = False
    list_select_related = True


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price"]
    show_full_result_count = False
    list_select_related = True


@admin.register(BookRating)
class BookRatingAdmin(admin.ModelAdmin):
    list_display = ["id", "book", "user", "rating"]
    show_full_result_count = False
    list_select_related = True
