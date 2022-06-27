from django.urls import re_path
from users import views

urlpatterns = [
    re_path(r'^users$', views.UserApi.as_view()),
    re_path(r'^users/([0-9]+)$', views.UserApi.as_view()),
    re_path(r'^auth$', views.AuthApi.as_view()),
]
