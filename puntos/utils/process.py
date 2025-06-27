import rasterio
from rasterio.transform import rowcol
def read_tif(tif,lat,lon):

    with rasterio.open(tif) as src:
        fila, columna = rowcol(src.transform, lon, lat)
        valor = src.read(1)[fila, columna]

    return valor