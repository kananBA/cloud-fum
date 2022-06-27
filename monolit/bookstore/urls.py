from django.urls import re_path
from bookstore import views

urlpatterns = [
    re_path(r'^users$', views.user_api),
    re_path(r'^users/([0-9]+)$', views.user_api),
    re_path(r'^books$', views.book_api),
    re_path(r'^books/([0-9]+)$', views.book_api),
    re_path(r'^reviews$', views.review_api),
    re_path(r'^reviews/([0-9]+)$', views.review_api),
    re_path(r'^orders$', views.order_api),
    re_path(r'^orders/([0-9]+)$', views.order_api),
]
