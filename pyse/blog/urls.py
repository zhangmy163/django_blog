from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('<int:post_id>/show', views.show, name='show'),
]