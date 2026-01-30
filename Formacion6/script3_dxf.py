import os.path
import json
import ezdxf
from ezdxf.colors import aci2rgb

archivo = "C:/Users/Agustin/Desktop/ficheros dxf/temperatura ambiente.dxf"


def Crear_Json():
    nombre, _ = os.path.splitext(archivo)
    doc = ezdxf.readfile(archivo)
    msp = doc.modelspace()
    entities = {}

    for e in msp:
        capa = e.dxf.layer
        tipo = e.dxftype()
        color = aci2rgb(e.dxf.color)

        if color is None:
            continue

        if capa not in entities:
            entities[capa] = {}

        if tipo not in entities[capa]:
            entities[capa][tipo] = list(color)

    with open(nombre + ".json", "w", encoding='utf-8') as f:
        json.dump(entities, f, ensure_ascii=False, indent=4)

    print(f"JSON creado: {nombre}.json")


Crear_Json()
