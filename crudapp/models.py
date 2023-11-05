from django.db import models

# Create your models here.

class Empleado(models.Model):
    emp_id = models.CharField(max_length=3, verbose_name="Id")
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    correo = models.EmailField(verbose_name="Email")
    designacion = models.CharField(max_length=150, verbose_name="Designación")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actuialización')

    class Meta:
        db_table = "Employee"
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"