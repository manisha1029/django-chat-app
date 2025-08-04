from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('<str:group_name>/', views.index, name='index'),
]