from django.contrib import admin
from django.urls import path,include
from web.views import get_monument

urlpatterns = [
    path('<str:id>/',view=get_monument),
]