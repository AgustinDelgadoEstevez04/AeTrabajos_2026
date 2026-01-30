import csv
from tokenize import String

from pyproj import Transformer
import math
import pandas as pd
ruta = "C:/Users/Agustin/Desktop/Ficheros tipo 1/400GUI-PGZ1_BACK.csv"
ruta2 = "C:/Users/Agustin/Desktop/Fichero tipo 1 copia/400GUI-PGZ1_BACK.csv"


def leer_csv():
    data = pd.read_csv(ruta, sep=None, engine="python")
    print(data.columns)

    for indice, row in data.iterrows():
        x = float(str(row["X"]).replace(",", ".").strip())
        y = float(str(row["Y"]).replace(",", ".").strip())

        lon, lat = transformar(x, y)
        epsg = "EPSG:" + str(get_real_epsg(lat, lon))
        new_x, new_y = transformar2(x, y, epsg)

        print(f"X: {new_x}   ||  Y:{new_y}")

        # Actualizar correctamente
        data.loc[indice, "X"] = new_x
        data.loc[indice, "Y"] = new_y

    data.to_csv(ruta2, sep=";", index=False)

    print("CSV se actualizó correctamente")


def transformar(x, y):
    transformer = Transformer.from_crs("EPSG:25830", "EPSG:4326", always_xy=True)
    lon, lat = transformer.transform(x, y)
    return lon, lat


def transformar2(x, y, epsg):
    transformer = Transformer.from_crs("EPSG:25830", epsg, always_xy=True)
    lon, lat = transformer.transform(x, y)
    return lon, lat


def get_real_epsg(latitude: float, longitude: float) -> int:
    if latitude > 0:
        epsg = 32600
    else:
        epsg = 32700

    epsg += math.trunc((longitude + 180) / 6) + 1
    return epsg


leer_csv()
