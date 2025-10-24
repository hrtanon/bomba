import random
import os


os.system("cls")


def zaklad():
    print(
        " mam pro tebe hru \n s jesnoduchymi pravidly kde hadas nahodne cislo 0 az 100\n   1. zadej cislo \n   2. dokud neuhodnes se nevzdavej"
    )
    potvrzeni = input(f"pokud chapes zmacni entr")

    if potvrzeni == "":
        a = nahodnecislo()
        obt = obtiznost()
        b = inpud()
        pocitadlo(a, b, obt)

    else:
        print(f"skoda tak nekdy priste")


def nahodnecislo():
    a = random.randint(0, 100)

    return a


def inpud():
    for i in range(2):
        try:
            b = int(input(f"nahodne cislo mam ted zadej tvuj typ"))
        except ValueError:
            print(
                f"pravidla byli zadat platne cislo \n ale ze si to ty tak ti dam jeste jednu sanci"
            )
            continue
    return b


def pocitadlo(a, b):
    list = []
    c = len(list)
    if a == b:
        print(f"jsi bocer vyhravas \n gratului")
        print(f"pocet pokusu {c}")

    elif a < b:
        print(f"cislo je mensi nez{b}")
        list.append(1)


def obtiznost():
    while True:
        try:
            x = int(
                input(
                    f"zvol obtiznost \n 1 pro pet pokusu-nemozna \n 2 pro 10-honde tezka \n 3 pro 15-uz by se dalo"
                )
            )
        except ValueError:
            print(f"zadat platne cislo")
            continue
        if x == 1:
            print("veris si")
            obt = 5
            return obt
        elif x == 2:
            print("to das")
            obt = 10
            return obt

        elif x == 3:
            print("tak pojdme na to")
            obt = 15
            return obt
        break
