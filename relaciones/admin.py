from django.contrib import admin
from .models import ModeloAuto,Fabricante,TipoCombustible,DirectorEjecutivo

# Register your models here.

admin.site.register(ModeloAuto)
admin.site.register(Fabricante)
admin.site.register(TipoCombustible)
admin.site.register(DirectorEjecutivo)
