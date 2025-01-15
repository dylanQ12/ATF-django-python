from django.urls import path
from .views import *

urlpatterns = [
    path("list/", ServiceListView, name="services"),
    path("create/", ServiceListView, name="create-service"),
]