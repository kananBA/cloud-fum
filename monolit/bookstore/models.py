from datetime import datetime
from django.db import models


# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    token = models.CharField(max_length=500)
    type = models.IntegerField(null=True)


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
    book = models.ForeignKey(Books, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)


class States(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    order_date = models.DateField(default=datetime.now, null=True)
    seller = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="seller_id", null=True)
    customer = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="customer_id", null=True)
    state = models.ForeignKey(States, on_delete=models.CASCADE, null=True)
