from django.urls import path     
from . import views
urlpatterns = [
	path('', views.session),
    path('destroy_session', views.destroy),
]