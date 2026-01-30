import ezdxf

archivo = "C:/Users/Agustin/Desktop/ficheros dxf/temperatura ambiente.dxf"


def listar_geometria():
    doc = ezdxf.readfile(archivo)
    msp = doc.modelspace()
    geometria = set()

    for m in msp:
        geometria.add(m.dxftype())

    print("Geometrias encontradas:")  # Capas
    for m in geometria:
        print(f" Geometria: {m}")


listar_geometria()
