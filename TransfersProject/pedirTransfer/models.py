from django.db import models

# Create your models here.
class Zona (models.Model):
    zonaId = models.BigAutoField(primary_key=True, verbose_name='Id de la zona')
    zonaName = models.CharField(max_length=50, verbose_name='Nombre de la zona')

    def __str__(self):
        return self.zonaName

class Comuna (models.Model):
    comId = models.BigAutoField(primary_key=True, verbose_name='Id de la comuna')
    comName = models.CharField(max_length=50, verbose_name='Nombre de la comuna')
    Zona = models.ForeignKey(Zona, on_delete=models.CASCADE)

    def __str__(self):
        return self.comName

class Transfer (models.Model):
    traPatent = models.CharField(primary_key=True, max_length=6, verbose_name='Patente del Transfer')
    traMarca = models.CharField(max_length=50, verbose_name='Marca del Transfer')
    traTamanio = models.CharField(max_length=25, verbose_name='Tamaño del Transfer')
    traDriver = models.CharField(max_length=50, verbose_name='Nombre del Chofer')
    traSeats = models.IntegerField(verbose_name='Cantidad Asientos del Transfer')
    traZona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    traParking = models.CharField(max_length=50, verbose_name='Estacionamiento del transfer', default='---')

    def __str__(self):
        return self.traPatent

class datosPasajero (models.Model):
    paId = models.BigAutoField(primary_key=True, verbose_name='Id de datos del pasajero')
    paCiudad = models.CharField(max_length=50, verbose_name='Ciudad')
    paComuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    paDireccion = models.CharField(max_length=80, verbose_name='Dirección')
    paSeats = models.IntegerField(verbose_name='Cantidad Asientos a Comprar', default=1)

    def __str__(self):
        return str(self.paId)