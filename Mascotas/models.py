from django.db import models
import datetime

# Create your models here.

class Productos(models.Model):
    dv = models.CharField(primary_key=True,max_length=5,verbose_name="Dv")
    nombre = models.CharField(max_length=50, blank=True, verbose_name="Nombre")
    descripcion = models.CharField(max_length=100, blank=True, verbose_name="Descripcion")
    cantidad = models.IntegerField(blank=True,verbose_name="Cantidad")
    precio= models.IntegerField(blank=True,verbose_name="Precio")
    imagen = models.ImageField(upload_to="imagenes",null=True,blank=True,verbose_name="Imagen")

    def __str__(self):
        return self.dv

class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
    
    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Productos', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)