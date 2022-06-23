from django.urls import path     
from . import views

app_name = 'fav_books'
urlpatterns = [
    path('', views.books),	
    path('add', views.add_book),
    path('<_id>', views.book_info),
    path('fav/<_id>', views.favorite),
    path('unfav/<_id>', views.unfavorite),
    path('update/<_id>', views.update),
    path('delete/<_id>', views.delete),
]