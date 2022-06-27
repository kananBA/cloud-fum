from rest_framework import serializers
from bookstore.models import Users, Books, Genres, Reviews, States, Orders


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'password', 'token', 'type')
        read_only_fields = ('id', 'token')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('id', 'name')


class BookSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        queryset=Genres.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Books
        fields = ('id', 'name', 'publisher', 'price', 'genre')


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('id', 'review_text', 'is_positive', 'book', 'user')


class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ('id', 'name')


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id', 'order_date', 'customer', 'seller', 'state')


class OrdersListSerializer(serializers.ModelSerializer):
    state = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Orders
        fields = ('id', 'order_date', 'customer', 'seller', 'state')
