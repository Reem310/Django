from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('',views.index , name="index"),
    path('new',views.new),
    path('create',views.create),
    path('<int:number>',views.show),
    path('<int:number>/edit',views.edit),
    path('<int:number>/delete',views.destroy)
]