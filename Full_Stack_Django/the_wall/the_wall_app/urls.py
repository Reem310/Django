from django.urls import path  
from django.urls.resolvers import URLPattern   
from . import views

app_name = 'the_wall'
urlpatterns = [
    path('', views.wall),
    path('post_msg', views.post_msg),
    path('post_comment', views.post_comment),
    path('delete/<_id>', views.delete_post),
]