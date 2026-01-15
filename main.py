from briofitas import Briofita
from pteridofitas import Pteridofita
from gimnospermas import Gimnosperma
from angiospermas import Angiosperma
from formulario import formulario


def mostrar_planta(planta):
    print(planta.caracteristicas())

if __name__ == "__main__":
    formulario()