from django.urls import path     
from . import views

app_name = 'reg_login'
urlpatterns = [
    path('', views.index),	
    path('reg', views.register),
    path('login', views.login),
    path('success', views.success),
    path('destroy', views.destroy),
]