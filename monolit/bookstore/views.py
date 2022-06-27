from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from bookstore.models import Users, Books, Reviews, Orders
from bookstore.serializers import UsersSerializer, BookSerializer, ReviewsSerializer,\
    OrdersSerializer, OrdersListSerializer


# Create your views here.
@csrf_exempt
def user_api(request, user_id=None):
    if request.method == 'GET':
        if user_id is None:
            users = Users.objects.all()
            users_serializer = UsersSerializer(users, many=True)
            return JsonResponse(users_serializer.data, safe=False)
        else:
            user = Users.objects.get(id=user_id)
            users_serializer = UsersSerializer(user)
            return JsonResponse(users_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        users_serializer = UsersSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("User has been added", safe=False)
        return JsonResponse(users_serializer.errors, safe=False)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = Users.objects.get(id=user_id)
        users_serializer = UsersSerializer(user, data=user_data, partial=True)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse(users_serializer.errors)
    elif request.method == 'DELETE':
        user = Users.objects.get(id=user_id)
        user.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def book_api(request, book_id=None):
    if request.method == 'GET':
        if book_id is None:
            books = Books.objects.all()
            books_serializer = BookSerializer(books, many=True)
            return JsonResponse(books_serializer.data, safe=False)
        else:
            book = Books.objects.get(id=book_id)
            books_serializer = BookSerializer(book)
            return JsonResponse(books_serializer.data, safe=False)

    elif request.method == 'POST':
        book_data = JSONParser().parse(request)
        books_serializer = BookSerializer(data=book_data)
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse("Book has been added", safe=False)
        return JsonResponse(books_serializer.errors, safe=False)

    elif request.method == 'PUT':
        book_data = JSONParser().parse(request)
        book = Books.objects.get(id=book_id)
        departments_serializer = BookSerializer(book, data=book_data, partial=True)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse(departments_serializer.errors, safe=False)
    elif request.method == 'DELETE':
        book = Books.objects.get(id=book_id)
        book.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def review_api(request, review_id=None):
    if request.method == 'GET':
        if review_id is None:
            reviews = Reviews.objects.all()
            reviews_serializer = ReviewsSerializer(reviews, many=True)
            return JsonResponse(reviews_serializer.data, safe=False)
        else:
            review = Reviews.objects.get(id=review_id)
            reviews_serializer = ReviewsSerializer(review)
            return JsonResponse(reviews_serializer.data, safe=False)

    elif request.method == 'POST':
        review_data = JSONParser().parse(request)
        reviews_serializer = ReviewsSerializer(data=review_data)
        if reviews_serializer.is_valid():
            reviews_serializer.save()
            return JsonResponse("Review has been added", safe=False)
        return JsonResponse(reviews_serializer.errors, safe=False)

    elif request.method == 'PUT':
        review_data = JSONParser().parse(request)
        review = Reviews.objects.get(id=review_id)
        reviews_serializer = ReviewsSerializer(review, data=review_data, partial=True)
        if reviews_serializer.is_valid():
            reviews_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse(reviews_serializer.errors)
    elif request.method == 'DELETE':
        review = Reviews.objects.get(id=review_id)
        review.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def order_api(request, order_id=None):
    if request.method == 'GET':
        if order_id is None:
            orders = Orders.objects.all()
            orders_serializer = OrdersListSerializer(orders, many=True)
            return JsonResponse(orders_serializer.data, safe=False)
        else:
            order = Orders.objects.get(id=order_id)
            orders_serializer = OrdersListSerializer(order)
            return JsonResponse(orders_serializer.data, safe=False)

    elif request.method == 'POST':
        order_data = JSONParser().parse(request)
        orders_serializer = OrdersSerializer(data=order_data)
        if orders_serializer.is_valid():
            orders_serializer.save()
            return JsonResponse("Order has been added", safe=False)
        return JsonResponse(orders_serializer.errors, safe=False)

    elif request.method == 'PUT':
        order_data = JSONParser().parse(request)
        order = Orders.objects.get(id=order_id)
        orders_serializer = OrdersSerializer(order, data=order_data, partial=True)
        if orders_serializer.is_valid():
            orders_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse(orders_serializer.errors)
    elif request.method == 'DELETE':
        order = Orders.objects.get(id=order_id)
        order.delete()
        return JsonResponse("Deleted Successfully", safe=False)
