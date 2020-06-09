from django.db.models import Avg
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book, BookRating
from books.serializers import BookSerializer, BookUpdateDeserializer, BookRatingSerializer, BookRatingDeserializer


class BookDetailView(APIView):
    permission_classes = (AllowAny,)

    def get(self, _request,book_id ):
        book = get_object_or_404(Book, id=book_id)
        data = BookSerializer(book).data
        return Response(data, status=status.HTTP_200_OK)


class BookView(APIView):
    permission_classes = (AllowAny,)

    def get(self, _request):
        book = Book.objects.all()
        data = BookSerializer(book, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(BookSerializer(data).data, status=status.HTTP_200_OK)

    def patch(self, request):
        book = get_object_or_404(Book, pk=request.data['id'])
        serializer = BookUpdateDeserializer(instance=book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(BookSerializer(data).data, status=status.HTTP_200_OK)

    def delete(self, request):
        book = get_object_or_404(Book, pk=request.data['id'])
        book.delete()
        return Response({"message": "Book with id `{}` has been deleted.".format(request.data['id'])}, status=204)


class BookRatingView(APIView):
    permission_classes = (AllowAny,)

    def get(self, _request):
        book = Book.objects.annotate(
            rating=Avg('reviews__rating')
        )
        data = BookRatingSerializer(book, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class BookRatingDetailView(APIView):
    permission_classes = (AllowAny,)

    def get(self, _request, book_id):
        book = Book.objects.filter(id=book_id).annotate(
            rating=Avg('reviews__rating')
        )
        data = BookRatingSerializer(book, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookRatingDeserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(BookRatingDeserializer(data).data, status=status.HTTP_200_OK)

    def patch(self, request):
        rating = get_object_or_404(BookRating, pk=request.data['id'])
        serializer = BookRatingDeserializer(instance=rating, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(BookRatingDeserializer(data).data, status=status.HTTP_200_OK)

    def delete(self, request):
        rating = get_object_or_404(BookRating, pk=request.data['id'])
        rating.delete()
        return Response({"message": "Rating has been deleted."}, status=204)
