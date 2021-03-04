from django.urls import path
from . import views

urlpatterns = [
    path('', views.getStatus),
    path('new', views.setStatus)
]
