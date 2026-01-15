from briofitas import Briofita
from pteridofitas import Pteridofita
from gimnospermas import Gimnosperma
from angiospermas import Angiosperma


def formulario():
    print("FORMULÁRIO PARA IDENTIFICAÇÃO DE PLANTAS ")

    flores = input("A planta que você procura possui flores? (s/n): ").lower()
    sementes = input("A planta que você procura possui sementes? (s/n): ").lower()

    if flores == "n" and sementes == "n":
        esporos = input("A planta se reproduz por esporos? (s/n): ").lower()

        if esporos == "s":
            print("Essa planta pode ser Briofita ou Pteridofita")
            print("Alguns exemplos:")
            print("Musgos (Briofitas)")
            print("Samambaias (Pteridofitas)")
        else:
            print("Planta não identificada.")

    elif flores == "s" and sementes == "s":
        frutos = input("A planta que você procura dá frutos? (s/n): ").lower()

        if frutos == "n":
            planta = Gimnosperma("Gimnosperma")
            print("Tipo identificado: ")
            print(planta.caracteristicas())

            print("Alguns exemplos: ")
            print("Pinheiro")
            print("Cipreste")

        elif frutos == "s":
            print("Responda com base nas características da planta:")

    nervos = input(
        "As folhas da planta têm nervos paralelos (Como se fosse fios igual tem no milho ou capim)? (s/n): "
    ).lower()

    if nervos == "s":
        tipo = "Monocotiledônea"
    elif nervos == "n":
        tipo = "Dicotiledônea"
    else:
        tipo = "Desconhecido"

    planta = Angiosperma("Angiosperma", tipo)

    print("Tipo identificado: ")
    print(planta.caracteristicas())

    print("Alguns exemplos: ")
    if tipo == "Monocotiledônea":
        print("Milho")
        print("Arroz")
        print("Capim")

    elif tipo == "Dicotiledônea":
        print("Feijão")
        print("Girassol")
        print("Roseira")
    else:
        print("Não foi possível identificar o tipo dessa planta.")



if __name__ == "__main__":
    formulario()
