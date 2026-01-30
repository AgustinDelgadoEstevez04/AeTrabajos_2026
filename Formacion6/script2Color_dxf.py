import ezdxf
from ezdxf.colors import aci2rgb

archivo = "C:/Users/Agustin/Desktop/ficheros dxf/temperatura ambiente.dxf"


def listar_color():
    doc = ezdxf.readfile(archivo)
    msp = doc.modelspace()

    print('Colores Encontrados:')
    colores = set()
    for m in msp:
        colores.add(m.dxf.color)

    diccionario = {}

    for color in colores:
        nombre = ACI_COLOR_NAMES.get(color)
        diccionario[color] = nombre

        print(f"{aci2rgb(color)} = {nombre}")


ACI_COLOR_NAMES = {
    1: "Rojo",
    2: "Amarillo",
    5: "Azul",
    7: "Blanco / Negro",
}
listar_color()
