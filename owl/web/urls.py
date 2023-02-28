from django.contrib import admin
from django.urls import path,include
from web.views import test

urlpatterns = [
    path('<str:id>/',view=test),
]