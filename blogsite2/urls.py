from django.urls import path
from .views import index,add,addregister

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('add/addregister/', addregister, name='addregister'),
]
