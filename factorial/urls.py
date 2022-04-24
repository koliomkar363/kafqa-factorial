from django.urls import path
from . import views

urlpatterns = [
    path('<int:num>/', views.index, name='index'),
    path('<str:input>/', views.error, name='error'),
]
