from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('baseCreate/', views.baseCreate, name="Create-Database"),
    path('baseLookup/<str:pk>/', views.baseLookup, name="IP-Lookup"),
]