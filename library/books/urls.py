from django.urls import re_path
from books import views

urlpatterns = [
    re_path(r'^books$', views.BookApi.as_view()),
    re_path(r'^books/([0-9]+)$', views.BookApi.as_view()),
    re_path(r'^genres$', views.GenreApi.as_view()),
    re_path(r'^genres/([0-9]+)$', views.GenreApi.as_view()),
    re_path(r'^reviews', views.ReviewApi.as_view()),
    re_path(r'^reviews/([0-9]+)$', views.ReviewApi.as_view()),
]
