from django.urls import path
from .views import index,add,addregister,delete,update,updateregister

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('add/addregister/', addregister, name='addregister'),
    path('delete/<int:id>/', delete, name='delete'),
    path('update/<int:id>/', update, name='update'),
    path('updateregister/<int:id>/', updateregister, name='updateregister'),

]
