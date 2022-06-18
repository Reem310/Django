from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('books/<_id>', views.books),
    path('authors', views.authors),
    path('authors/<_id>', views.new_author),
]