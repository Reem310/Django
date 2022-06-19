from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('shows', views.all_shows),	
    path('shows/new', views.new),
    path('shows/create', views.add_show),
    path('shows/<_id>', views.show),
    path('shows/<_id>/edit', views.update),
    path('shows/<_id>/update', views.edit),		
    path('shows/<_id>/destroy', views.destroy),	
]