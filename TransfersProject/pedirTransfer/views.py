from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import forms
from django.db.models import Q

# Create your views here.
def index (request):
    if request.method == 'POST':
        datos_form = forms.datosForm(request.POST)
        if datos_form.is_valid():
            datos_form.save()
            
            idDatos = models.datosPasajero.objects.latest('paId')

            cantAsientos  = request.POST["paSeats"]
            comunaPa = request.POST["paComuna"]
            comuna = models.Comuna.objects.get(comId=comunaPa)
            zona = comuna.Zona
            cri1 = Q(traZona__zonaName__icontains=zona)
            cri2 = Q(traSeats__gte=cantAsientos)
            transfers = models.Transfer.objects.filter(cri1 & cri2)
            return render(request, "escogerTransfer.html", {"transfers":transfers, "query":zona, "datos":idDatos})
    else:
        datos_form = forms.datosForm()
    return render(request, "index.html", {'datos_form': datos_form})

def delDatos (request, id):
    datos = models.datosPasajero.objects.get(paId=id)
    datos.delete()
    return redirect('index')

def selecPago (request, idPatente, idDatos):
    return render(request, "selecPago.html", {"idPatente":idPatente,"idDatos":idDatos})

def datos (request, idPatente, idDatos):
    context={
        'transfer':models.Transfer.objects.filter(traPatent__icontains=idPatente),
        'datosPa':models.datosPasajero.objects.filter(paId=idDatos)
    }
    return render(request, "ticket.html", context)


# ESTO NO LO USO --->
# def buscar(request):
#     if request.method == 'POST':
#         datos_form = forms.datosForm(request.POST)
#         if datos_form.is_valid():
#             datos_form.save()

#     comunaPa = request.POST["paComuna"]
#     comuna = models.Comuna.objects.get(comId=comunaPa)

#     zona = comuna.Zona

#     transfers = models.Transfer.objects.filter(traZona__zonaName__icontains=zona)
        
#     return render(request, "escogerTransfer.html", {"transfers":transfers, "query":zona})


# def edad(request,anio):
#     act=19
#     periodo=anio-2022
#     years=act+periodo
#     document="""
#         <html>
#         <body>
#             <h1>En el año %s tu edad sería %s </h1>
#         </body>
#         </html>
#     """ %(anio, years)


#     return HttpResponse(document)