from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

from .models import Empleado

# Create your tests here.

class EmpleadoTest(TestCase):
    databases="__all__"
    @classmethod
    def setUpTestData(cls):
        cls.empleado = Empleado.objects.create(
            emp_id="123",
            nombre="Juan",
            correo="Juan@conce.cl",
            designacion="Desarrollo Web"
        )

    def test_model_content(self):
        self.assertEqual(self.empleado.emp_id,"123")
        self.assertEqual(self.empleado.nombre,"Juan")
        self.assertEqual(self.empleado.correo,"Juan@conce.cl")
        self.assertEqual(self.empleado.designacion,"Desarrollo Web")

    def test_url_exists_at_correct_location(self):
        response = self.client.get('/crudapp/')
        self.assertEqual(response.status_code,200)

    def test_homepage(self):
        response = self.client.get(reverse('mostrar'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'crudapp/mostrar.html')
        self.assertContains(response,'Designación')




class MostrarTest(SimpleTestCase):

    databases = '__all__'

    def test_url_exists_at_correct_location(self):
        response = self.client.get('/crudapp/mostrar/')
        self.assertEqual(response.status_code,200) #el status code cuando nos conectamos == 200

    def test_url_available_by_name(self):
        response = self.client.get(reverse('mostrar'))
        self.assertEqual(response.status_code,200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('mostrar'))
        self.assertTemplateUsed(response,'crudapp/mostrar.html')
    
    def test_template_content(self):
        response = self.client.get(reverse('mostrar'))
        self.assertContains(response,'<th scope="col">Id de Empleado</th>')
        self.assertNotContains(response,'<h1>HOLA MUNDO</h1>')