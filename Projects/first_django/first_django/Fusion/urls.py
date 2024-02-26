from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("todotask", views.todotask, name="todotask"),
    path("add", views.add, name="add"),
    path("<str:name>", views.greet, name="greet")

]