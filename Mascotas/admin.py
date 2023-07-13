from django.contrib import admin
from .models import Productos,detalle_boleta,Boleta

# Register your models here.
admin.site.register(Productos)
admin.site.register(detalle_boleta)
admin.site.register(Boleta)