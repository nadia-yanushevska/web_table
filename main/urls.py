from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
path("", views.index, name = "index"),
path("home/", views.index, name = "index"),
path("create/", views.create, name = "create"),
path("media/<str:name>.csv", views.table_csv, name = "table_csv"),
path("home/media/<str:name>.csv", views.table_csv, name = "table_csv"),
path("",  include("django.contrib.auth.urls")),

]