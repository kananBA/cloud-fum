from rest_framework import serializers
from books.models import Books, Genres, Reviews


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
