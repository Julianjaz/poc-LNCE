from django.urls import path
from .views import PuntoListCreateView, procesar_coordenadas

urlpatterns = [
    path('puntos/', PuntoListCreateView.as_view(), name='puntos'),
    path('procesar-coordenadas/', procesar_coordenadas, name='procesar-coordenadas'),
]