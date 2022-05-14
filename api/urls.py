from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('update/<str:pk>/', views.updateItem),
    path('get/<str:pk>/', views.getItem),
    path('delete/<str:pk>/', views.Delete)
]