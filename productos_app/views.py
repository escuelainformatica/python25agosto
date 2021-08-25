from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from productos_app.models import Producto
# Create your views here.


# ????? como lo puedo probar????

def formulario_sumar(request):
    # usar get cuando se carga el formulario la primera vez.
    # user post cuando se carga el formulario despues de que el usuario envio datos
    if request.method=='GET':
        num1=0
        num2=0
    else:
        num1=int(request.POST['num1'])
        num2=int(request.POST['num2'])
    total=num1+num2
    context={"num1":num1,"num2":num2,"total":total}
    return render(request,'productos/formulario_sumar.html',context)


def listar(request):
    productos=Producto.objects.all() # leer todos los datos desde la entidad producto
    context={"productos":productos}
    return render(request,'productos/listar.html',context)


def index(request):
    template = loader.get_template('miapp/index.html')
    context = {
        'paises':["chile","argentina","peru"],
        'nombre':'hola mundo'
    }
    return HttpResponse(template.render(context, request))