from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('total', views.total),
    path('checkout', views.checkout),
]
