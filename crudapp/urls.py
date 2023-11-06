
from django.urls import path
from . import views


urlpatterns = [
    path("", views.insertar, name="insertar"),
    path("mostrar/", views.mostrar, name="mostrar"),
    path("editar/<int:pk>/", views.editar, name="editar"),
    path("eliminar/<int:pk>/", views.eliminar, name="eliminar"),
    path("empleado/<int:pk>/", views.empleado_detalle_view, name='empleado_detalle'),

]
