import math
from math import radians, sin, cos, sqrt, atan2
from decimal import Decimal

def haversine(lat1, lon1, lat2, lon2):
    rad=Decimal(math.pi/180)
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia



def calcular_distancia(lat1, lon1, lat2, lon2):
    # Radio de la Tierra en metros
    radio_tierra = 6371000

    # Convertir latitudes y longitudes a radianes
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    # Diferencias de latitud y longitud
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Fórmula de Haversine
    a = sin(dlat/2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distancia = radio_tierra * c

    return distancia