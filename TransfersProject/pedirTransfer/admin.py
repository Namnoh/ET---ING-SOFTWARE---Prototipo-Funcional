from django.contrib import admin
from . import models

class ZonaAdmin(admin.ModelAdmin):
    search_fields = ['zonaId', 'zonaName'],
    ordering = ['zonaName']

class ComunaAdmin(admin.ModelAdmin):
    search_fields = ['comId', 'comName'],
    autocomplete_fields = ['Zona']
    ordering = ['comName']

class TransferAdmin(admin.ModelAdmin):
    autocomplete_fields = ['traZona']

class datosAdmin(admin.ModelAdmin):
    autocomplete_fields = ['paComuna']

# Register your models here.
admin.site.register(models.Zona, ZonaAdmin)
admin.site.register(models.Comuna, ComunaAdmin)
admin.site.register(models.Transfer, TransferAdmin)
admin.site.register(models.datosPasajero, datosAdmin)