from django.urls import path
from .views import index,vision,tienda,adopcion,registrar,crear,modificar,eliminar,generarBoleta,agregar_producto,eliminar_producto,restar_producto,limpiar_carrito

urlpatterns = [
    path('', index, name="index"),
    path('vision/', vision, name="vision"),
    path('tienda/', tienda, name="tienda"),
    path('adopcion/', adopcion, name="adopcion"),
    path('registrar/', registrar, name="registrar"),
    path('crear/', crear, name="crear"),
    path('modificar/<id>', modificar, name="modificar"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
]
 