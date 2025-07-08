from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Punto
from .serializers import PuntoSerializer
from puntos.utils.process import read_tif
from puntos.uses_cases.water_potencial import WaterPotencial
from puntos.uses_cases.biomass_potencial import BiomassPotencial

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
    value_q = read_tif("/Users/julianatehortuazapata/Desktop/github/poc-LNCE/puntos/data/caudal.tif", lat, lng)
    nivel = request.data.get('nivel', 'media')
    p_w = WaterPotencial().calculate(value_q,nivel)
    ###########################

    ###########################
    ######### Biomasa #########
    ###########################
    value_ren = read_tif("/Users/julianatehortuazapata/Desktop/github/poc-LNCE/puntos/data/aguacate.tif", lat, lng)
    area = float(request.data.get('area', 0))
    p_b = BiomassPotencial().calculate(area,value_ren)
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
        'P_biomass': p_b,
        'guardado_como': punto.nombre
    })