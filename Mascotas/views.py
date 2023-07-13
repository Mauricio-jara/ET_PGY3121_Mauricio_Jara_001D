from django.shortcuts import render, redirect
from .models import Productos,Boleta,detalle_boleta
from .forms import ProductosForm, RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from Mascotas.compra import Carrito
import os

# Create your views here.
def index(request):
     return render(request, 'index.html')

def vision(request):
     return render(request, 'vision.html')

def tienda(request):
     productos = Productos.objects.all()
     datos={
        'productos':productos
    }
     return render(request,'tienda.html',datos)

def adopcion(request):
     return render(request, 'adopcion.html')

def registrar(request):
     data={
        'form':RegistroUserForm()
     }
     if request.method=="POST":
          formulario = RegistroUserForm(data=request.POST)
          if formulario.is_valid():
               formulario.save()
               user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
               login(request,user)
               return redirect ('index')
          data["form"] = formulario
     return render(request, 'registration/registrar.html',data)

@login_required
def crear(request):
    if request.method=="POST":
        productosform = ProductosForm(request.POST, request.FILES)
        if productosform.is_valid():
            productosform.save()     #similar al insert
            return redirect('tienda')
    else:
        productosform=ProductosForm()
    return render(request, 'crear.html', {'productosform':productosform})

@login_required
def modificar(request, id):
     producto = Productos.objects.get(dv=id)
     if request.method=='POST':
          if len(request.FILES)!=0:
               if len(producto.imagen)>0:
                    os.remove(producto.imagen.path)
               producto.imagen=request.FILES['imagen']
          producto.nombre=request.POST.get('nombre')
          producto.descripcion=request.POST.get('descripcion')
          producto.save()
          return redirect('tienda')
     datos = {
          'form': ProductosForm(request.POST,request.FILES,instance=producto)
     }
     return render(request, 'modificar.html', datos)

@login_required
def eliminar(request, id):
    productoEliminado = Productos.objects.get(dv=id) #obtenemos un objeto por su id
    productoEliminado.delete()
    return redirect ('tienda')

def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    producto = Productos.objects.get(dv=id)
    carrito_compra.agregar(producto=producto)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Productos.objects.get(dv=id)
    carrito_compra.eliminar(producto=producto)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Productos.objects.get(dv=id)
    carrito_compra.restar(producto=producto)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')    

@login_required
def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Productos.objects.get(dv = value['producto_id'])
            cant = value['cantidad']
            producto.cantidad=producto.cantidad-cant
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            producto.save()
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)