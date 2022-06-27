from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
import requests

from books.models import Books, Reviews, Genres
from books.serializers import BookSerializer, ReviewsSerializer, GenreSerializer


# Create your views here.
class BookApi(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, book_id=None):
        if book_id is None:
            books = Books.objects.all()
            books_serializer = BookSerializer(books, many=True)
            return JsonResponse(books_serializer.data, safe=False)
        else:
            book = Books.objects.get(id=book_id)
            books_serializer = BookSerializer(book)
            return JsonResponse(books_serializer.data, safe=False)

    def post(self, request):
        book_data = JSONParser().parse(request)
        books_serializer = BookSerializer(data=book_data)
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse("Book has been added", safe=False)
        return JsonResponse(books_serializer.errors, safe=False)

    def put(self, request, book_id):
        book_data = JSONParser().parse(request)
        book = Books.objects.get(id=book_id)
        departments_serializer = BookSerializer(book, data=book_data, partial=True)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse(departments_serializer.errors, safe=False)

    def delete(self, request, book_id):
        book = Books.objects.get(id=book_id)
        book.delete()
        return JsonResponse("Deleted Successfully", safe=False)


class GenreApi(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, genre_id=None):
        if genre_id is None:
            genres = Genres.objects.all()
            genres_serializer = GenreSerializer(genres, many=True)
            return JsonResponse(genres_serializer.data, safe=False)
        else:
            genre = Genres.objects.get(id=genre_id)
            genres_serializer = GenreSerializer(genre)
            return JsonResponse(genres_serializer.data, safe=False)

    def post(self, request):
        auth = requests.get('http://user.management:8000/api/auth', headers={
            'Authorization': f'{request.headers["Authorization"]}'
        })

        try:
            if auth.json()['success']:
                genre_data = JSONParser().parse(request)
                genres_serializer = GenreSerializer(data=genre_data)
                if genres_serializer.is_valid():
                    genres_serializer.save()
                    return JsonResponse("Genre has been added", safe=False)
                return JsonResponse(genres_serializer.errors, safe=False)
        except KeyError as err:
            print(err)
        return HttpResponse(auth)

    def delete(self, request, genre_id):
        auth = requests.get('http://user.management:8000/api/auth', headers={
            'Authorization': f'{request.headers["Authorization"]}'
        })

        try:
            if auth.json()['success']:
                genre = Genres.objects.get(id=genre_id)
                genre.delete()
                return JsonResponse("Deleted Successfully", safe=False)
        except KeyError as err:
            print(err)
        return HttpResponse(auth)


class ReviewApi(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, review_id=None):
        if review_id is None:
            reviews = Reviews.objects.all()
            reviews_serializer = ReviewsSerializer(reviews, many=True)
            return JsonResponse(reviews_serializer.data, safe=False)
        else:
            review = Reviews.objects.get(id=review_id)
            reviews_serializer = ReviewsSerializer(review)
            return JsonResponse(reviews_serializer.data, safe=False)

    def post(self, request):
        auth = requests.get('http://user.management:8000/api/auth', headers={
            'Authorization': f'{request.headers["Authorization"]}'
        })

        try:
            if auth.json()['success']:
                review_data = JSONParser().parse(request)
                reviews_serializer = ReviewsSerializer(data=review_data)
                if reviews_serializer.is_valid():
                    reviews_serializer.save()
                    return JsonResponse("Review has been added", safe=False)
                return JsonResponse(reviews_serializer.errors, safe=False)
        except KeyError as err:
            print(err)
        return HttpResponse(auth)

    def put(self, request, review_id):
        auth = requests.get('http://user.management:8000/api/auth', headers={
            'Authorization': f'{request.headers["Authorization"]}'
        })

        try:
            if auth.json()['success']:
                review_data = JSONParser().parse(request)
                review = Reviews.objects.get(id=review_id)
                reviews_serializer = ReviewsSerializer(review, data=review_data, partial=True)
                if reviews_serializer.is_valid():
                    reviews_serializer.save()
                    return JsonResponse("Updated Successfully", safe=False)
                return JsonResponse(reviews_serializer.errors)
        except KeyError as err:
            print(err)
        return HttpResponse(auth)

    def delete(self, request, review_id):
        auth = requests.get('http://user.management:8000/api/auth', headers={
            'Authorization': f'{request.headers["Authorization"]}'
        })

        try:
            if auth.json()['success']:
                review = Reviews.objects.get(id=review_id)
                review.delete()
                return JsonResponse("Deleted Successfully", safe=False)
        except KeyError as err:
            print(err)
        return HttpResponse(auth)
