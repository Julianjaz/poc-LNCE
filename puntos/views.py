from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Punto
from .serializers import PuntoSerializer
from puntos.utils.process import read_tif
from puntos.uses_cases.water_potencial import WaterPotencial
from puntos.uses_cases.biomass_potencial import BiomassPotencial
from puntos.uses_cases.solar_potencial import SolarPotencial
from puntos.uses_cases.wind_potencial import WindPotencial

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

    ###########################
    ######### Solar #########
    ###########################
    value_sb = read_tif("/Users/julianatehortuazapata/Desktop/github/poc-LNCE/puntos/data/radiacion_sb.tif", lat, lng)
    value_re = read_tif("/Users/julianatehortuazapata/Desktop/github/poc-LNCE/puntos/data/radiacion_re.tif", lat, lng)
    value_t2m = read_tif("/Users/julianatehortuazapata/Desktop/github/poc-LNCE/puntos/data/T2M_mean.tif", lat, lng)
    area = float(request.data.get('area', 0))
    p_s = SolarPotencial().calculate(area,value_re,value_sb,value_t2m)
    ###########################

    ###########################
    ######### Wind #########
    ###########################
    value_ps = read_tif("/Users/julianatehortuazapata/Desktop/github/poc-LNCE/puntos/data/PS_mean.tif", lat, lng)
    value_vel = read_tif("/Users/julianatehortuazapata/Desktop/github/poc-LNCE/puntos/data/wind_speed_COL_10.tif", lat, lng)
    value_t2m = read_tif("/Users/julianatehortuazapata/Desktop/github/poc-LNCE/puntos/data/T2M_mean.tif", lat, lng)
    altura_buje = float(request.data.get('altura_buje', 0))
    alpha = float(request.data.get('alpha', 0))
    coef_friccion = float(request.data.get('coef_friccion', 0))
    p_w = WindPotencial().calculate(value_ps, value_t2m, value_vel, altura_buje, alpha, coef_friccion)
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
        'P_solar': p_s,
        'P_wind': p_w,
        'guardado_como': punto.nombre
    })