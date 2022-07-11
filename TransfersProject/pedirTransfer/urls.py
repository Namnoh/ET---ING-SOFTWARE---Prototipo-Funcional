from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #path('buscar/', views.buscar, name='buscar'),
    path('delDatos/<id>', views.delDatos, name='delDatos'),
    path('selecPago/<str:idPatente>/<int:idDatos>', views.selecPago, name='selecPago'),
    path('ticket/<str:idPatente>/<int:idDatos>', views.datos, name='datos'),
]