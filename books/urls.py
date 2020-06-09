from django.urls import path, include

from books.views import BookView, BookRatingView, BookDetailView, BookRatingDetailView

urlpatterns = [
    path("", BookView.as_view(), name='book-list'),
    path("ratings/", BookRatingView.as_view(), name="books-rating"),
    path("<int:book_id>/", include(
        [path("", BookDetailView.as_view(), name='book-detail'),
         path("ratings/", BookRatingDetailView.as_view(), name="book-rating-detail", ),
         ]),
         )
]
