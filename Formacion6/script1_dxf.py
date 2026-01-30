import ezdxf

archivo = "C:/Users/Agustin/Desktop/ficheros dxf/temperatura ambiente.dxf"


def listar_capas():
    doc = ezdxf.readfile(archivo)
    msp = doc.modelspace()
    capas = set()
    # Capas
    for m in msp:
        capas.add(m.dxf.layer)

    print("Capas encontradas:")
    for capa in sorted(capas):
        print(f"{capa}")


listar_capas()
