import xlwt
from pyproj import Transformer
import math
import pandas as pd
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

ruta = "C:/Users/Agustin/Desktop/Ficheros tipo 2/0667_220CAR-DRO_AnomaliasInfraestruturas2024.xls"
ruta2 = "C:/Users/Agustin/Desktop/Ficheros tipo 2 copia/0667_220CAR-DRO_AnomaliasInfraestruturas2024.xls"


def xls():
    data = pd.read_excel(ruta, dtype=str, engine='xlrd')

    for indice, row in data.iterrows():
        x = float(str(row["X"]).replace(",", ".").strip())
        y = float(str(row["Y"]).replace(",", ".").strip())
        H = str(row["HUSO"]).strip()
        epsg = int("258" + H)
        print(f"viejos ||X: {x}   ||  Y:{y}")

        # origen → 4326 (solo para calcular EPSG real)
        lon, lat = transformar_a_4326(x, y, epsg)
        epsg_real = get_real_epsg(lat, lon)

        # origen → destino directo
        new_x, new_y = transformar(x, y, epsg, epsg_real)

        ultimos_EPSG = str(epsg_real)[-2:]

        print(f"NUEVOS ||X: {new_x}   ||  Y:{new_y}")

        data.loc[indice, "X"] = new_x
        data.loc[indice, "Y"] = new_y
        data.loc[indice, "HUSO"] = int(ultimos_EPSG)

    guardar_xls_con_hipervinculo(data, ruta2)


def guardar_xls_con_hipervinculo(dataframe, ruta_salida):
    # Guarda DataFrame como .xls con fórmulas HIPERVINCULO
    libro = xlwt.Workbook()
    hoja = libro.add_sheet('Hoja1')

    # Encontrar índice de columnas
    evidencia = list(dataframe.columns).index("Evidencia Gráfica")
    anomalia = list(dataframe.columns).index("Nº Anomalia SAP")

    # Escribir cabeceras
    for indice_columna, nombre_col in enumerate(dataframe.columns):
        hoja.write(0, indice_columna, nombre_col)

    # Escribir datos
    for indice_fila, fila in enumerate(dataframe.values, start=1):
        for indice_columna, valor in enumerate(fila):
            if indice_columna == evidencia:
                # Crear fórmula HIPERVINCULO
                num_anomalia = fila[anomalia]
                formula = f'HYPERLINK("{num_anomalia}.jpg";"Imagen")'
                hoja.write(indice_fila, indice_columna, xlwt.Formula(formula))
            else:
                hoja.write(indice_fila, indice_columna, valor)

    libro.save(ruta_salida)
    print(f"Archivo guardado en: {ruta_salida}")

def transformar_a_4326(x, y, epsg):
    transformer = Transformer.from_crs(epsg, "EPSG:4326", always_xy=True)
    lon, lat = transformer.transform(x, y)
    return lon, lat


def transformar(x, y, epsg, epsg_destino):
    transformer = Transformer.from_crs(epsg, epsg_destino, always_xy=True)
    new_x, new_y = transformer.transform(x, y)
    return new_x, new_y


def get_real_epsg(latitude: float, longitude: float) -> int:
    if latitude > 0:
        epsg = 32600
    else:
        epsg = 32700
    epsg += math.trunc((longitude + 180) / 6) + 1
    return epsg


xls()