from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Punto
from .serializers import PuntoSerializer
from puntos.utils.process import read_tif
from puntos.uses_cases.water_potencial import WaterPotencial

class PuntoListCreateView(generics.ListCreateAPIView):
    queryset = Punto.objects.all()
    serializer_class = PuntoSerializer

@api_view(['POST'])
def procesar_coordenadas(request):
    lat = float(request.data.get('lat', 0))
    lng = float(request.data.get('lng', 0))
    ###########################
    ######### Hidrico #########
    ###########################
    value_q = read_tif("/Users/julianatehortuazapata/Downloads/mapa_django_app2/puntos/data/caudal.tif", lat, lng)
    nivel = request.data.get('nivel', 'media')
    p_w = WaterPotencial().calculate(value_q,nivel)
    ###########################

    punto = Punto.objects.create(
        nombre="Punto generado",
        descripcion="Coordenadas desde clic",
        latitud=lat,
        longitud=lng
    )

    return Response({
        'lat_original': lat,
        'lng_original': lng,
        'P_hidrico': p_w,
        'guardado_como': punto.nombre
    })