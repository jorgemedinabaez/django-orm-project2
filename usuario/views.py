from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout

from .forms import RegistroUsuario


# Create your views here.

def registro_view(request):
    if request.method == 'POST':
        form = RegistroUsuario(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,'Registro satisfactorio.')
            return HttpResponseRedirect('/crudapp/mostrar/')
        messages.error(request,'Registro inválido. Algunos datos son incorrectos')
    form = RegistroUsuario()
    context = {'register_form':form}
    return render(request,'usuario/registro.html',context)
