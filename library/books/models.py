from django.db import models


# Create your models here.
class Genres(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    publisher = models.CharField(max_length=500, null=True)
    price = models.IntegerField(null=True)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE, null=True)


class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    review_text = models.CharField(max_length=500)
    is_positive = models.IntegerField(null=True)
    user = models.IntegerField(null=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, null=True)
