import random
import os


os.system("cls")
random.seed()

def zaklad():
    print(
        " mam pro tebe hru \n s jesnoduchymi pravidly kde hadas nahodne cislo 0 az 100\n   1. zadej cislo \n   2. dokud neuhodnes se nevzdavej"
    )
    potvrzeni = input(f"pokud chapes zmacni entr")

    if potvrzeni == "":
        a = nahodnecislo()
        obt = obtiznost()
        telo_hry(a,obt)

    else:
        print(f"skoda tak nekdy priste")


def nahodnecislo():
    random.seed()
    a = random.randint(0, 100)

    return a

def cislo():

    for i in range(2):
        try:
            b = int(input(f"nahodne cislo mam ted zadej tvuj typ"))
            break
        except ValueError:
            print(
                    f"pravidla byli zadat platne cislo \n ale ze si to ty tak ti dam jeste jednu sanci"
                )
            continue
    return b



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


def telo_hry(a,obt):
    

    for i in range(obt):
        b=cislo()
        if a == b:
            print(f"jsi bocer vyhravas \n gratului")
            print(f"pocet pokusu {i+1}")
            print(a)
            return

        elif a < b:
            print(f"cislo je mensi nez{b}")
            continue
        elif a > b:
            print(f"cislo je vetsi nez{b}")
            continue
    print(f"treba priste")
    return 


for i in range(10):
    zaklad()




# čela funce nema osetreny spravne vsup nevidel jsem cislo vetsi nez 20 vylosovano a kdyz zadam cislo jednociferne nespousti
# se ta if podminka a nepise mi nic nefunguje loop nekdy se sam neukonci dokud nevyhraji

