from django.contrib import admin
from django.urls import path,include
from web.views import get_monument,get_monuments_from_slug

urlpatterns = [
    path('<int:id>/',view=get_monument),
    path('<slug:slug>/', view=get_monuments_from_slug),
]