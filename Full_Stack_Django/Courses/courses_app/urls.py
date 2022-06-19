from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add_course),
    path('courses/destroy/<_id>', views.delete_option),
    path('destroy/<_id>', views.destroy),
]