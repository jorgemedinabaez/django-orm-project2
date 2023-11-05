
from django.urls import path
from . import views


urlpatterns = [
    path("", views.insertar, name="insertar"),
    path("", views.mostrar, name="mostrar"),
    path("", views.editar, name="editar"),
    path("", views.eliminar, name="eliminar"),

]
