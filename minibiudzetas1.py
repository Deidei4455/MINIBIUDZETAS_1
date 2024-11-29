import pickle
import funkcijos

try:
    with open("Pajamos.pickle", mode="rb") as file:
        pajamos = pickle.load(file)
except FileNotFoundError:
    pajamos = []

try:
    with open("Islaidos.pickle", mode="rb") as file:
        islaidos = pickle.load(file)
except FileNotFoundError:
    islaidos = []

print("Sveiki atvyke į minibiudžeto programą")
input("Tęskite su enter ")
print("-----------------------------")
while True:
    print("Pagrindinis meniu\n"
          "1 - Įvesti pajamas\n"
          "2 - Įvesti išlaidas\n"
          "3 - Atspausdinti pajamų eilutes\n"
          "4 - Atspausdinti išlaidų eilutes\n"
          "5 - Atspausdinti statistiką\n"
          "6 - Ištrinti pasirinktas pajamas arba išlaidas\n"
          "7 - Paieška, ką norėtumėte pamatyti\n"
          "q - Išeiti iš programos")
    pasirinkimas = input("> ")
    if pasirinkimas == "1":
        data_pajamos = input("Įveskite pajamų datą: ")
        pajamu_saltinis = input("Įveskite pajamų tipą (atlyginimas, stipendija ...): ")
        pajamu_suma = int(input("Įveskite pajamų sumą: "))
        pajamu_tipas = [data_pajamos, pajamu_saltinis, pajamu_suma]
        pajamos.append(pajamu_tipas)
        print(f"Įvestos pajamos {pajamu_tipas}")
        input("Tęskite su enter ")
    elif pasirinkimas == "2":
        data_islaidos = input("Įveskite išlaidų datą: ")
        islaidu_name = input("Įveskite išlaidų pavadinimą (maistas, būstas ...): ")
        islaidu_suma = int(input("Įveskite išlaidų sumą: "))
        islaidu_tipas = [data_islaidos, islaidu_name, islaidu_suma]
        islaidos.append(islaidu_tipas)
        print(f"Įvestos išlaidos {islaidu_tipas}")
        input("Tęskite su enter ")
    elif pasirinkimas == "3":
        for elem in pajamos:
            print(f"data: {elem[0]}, pajamų tipas: {elem[1]}, {elem[2]}")
        input("Tęskite su enter ")
    elif pasirinkimas == "4":
        for elem in islaidos:
            print(f"data: {elem[0]}, išlaidų tipas: {elem[1]}, {elem[2]}")
        input("Tęskite su enter ")
    elif pasirinkimas == "5":
        while True:
            print("Pasirinkite, ką norėtumėte sužinoti\n"
                  "1 - Pajamų informacija\n"
                  "2 - Išlaidų statistikos\n"
                  "q - Grįžti atgal")
            Statistikos_pasirinkimas = input("> ")
            if Statistikos_pasirinkimas == "1":
                eilutes_max = funkcijos.gauk_maximuma(pajamos)
                eilutes_min = funkcijos.gauk_minimuma(pajamos)
                eilutes_suma = funkcijos.gauk_bendra_suma(pajamos)
                eilutes_avg = funkcijos.gauk_vidurki(pajamos)
                for elem in eilutes_max:
                    print(f"Didžiausios pajamos, data: {elem[0]}. {elem[1]}: {elem[2]}")
                for elem in eilutes_min:
                    print(f"Mažiausios pajamos, data: {elem[0]}. {elem[1]}: {elem[2]}")
                print(f"Visų pajamų suma - {eilutes_suma}")
                print(f"Visų pajamų vidurkis - {eilutes_avg}")
                input()
            elif Statistikos_pasirinkimas == "2":
                islaidos_max = funkcijos.gauk_maximuma(islaidos)
                islaidos_min = funkcijos.gauk_minimuma(islaidos)
                islaidos_suma = funkcijos.gauk_bendra_suma(islaidos)
                islaidos_avg = funkcijos.gauk_vidurki(islaidos)
                for elem in islaidos_max:
                    print(f"Didžiausios išlaidos, data: {elem[0]}. {elem[1]}: {elem[2]}")
                for elem in islaidos_min:
                    print(f"Mažiausios išlaidos, data: {elem[0]}. {elem[1]}: {elem[2]}")
                print(f"Visų išlaidų suma - {islaidos_suma}")
                print(f"Visų išlaidų vidurkis - {islaidos_avg}")
                input()
            elif Statistikos_pasirinkimas == "q":
                break
    elif pasirinkimas == "6":
        while True:
            print("1 - Trinti pajamų sąraše esančias pajamas\n"
                  "2 - Trinti išladių sąraše esančias išlaidas\n"
                  "q - Eiti atgal")
            Trynimo_pasirinkimas = input("> ")
            if Trynimo_pasirinkimas == "1":
                for elem in enumerate(pajamos):
                    print(elem)
                indeksas = int(input("Įveskite skaičių, indeksuojantį, kurias pajamas pašalinti: "))
                pajamos.remove(pajamos[indeksas])
                print(pajamos)
                input()
            elif Trynimo_pasirinkimas == "2":
                for elem in enumerate(islaidos):
                    print(elem)
                indeksas = int(input("Įveskite skaičių, indeksuojantį, kurias išlaidas pašalinti: "))
                islaidos.remove(islaidos[indeksas])
                print(islaidos)
                input()
            elif Trynimo_pasirinkimas == "q":
                break
    elif pasirinkimas == "7":
        Paieska_pasirinkimas = input("Įveskite raktažodį, ką norite surasti (pvz. stipendija, maistas ...): ")
        for elem in pajamos:
            if Paieska_pasirinkimas in elem:
                print(elem[0], elem[1], elem[2])
            else:
                print("Raktažodis nerastas!!")
        for elem in islaidos:
            if Paieska_pasirinkimas in elem:
                print(elem[0], elem[1], elem[2])
            else:
                print("Raktažodis nerastas!!")
        input("Tęskite su enter ")
    elif pasirinkimas == "q":
        print("Išėjote iš programos")
        break
print(pajamos)
print(islaidos)

with open("Pajamos.pickle", mode="wb") as file:
    # noinspection PyTypeChecker
    pickle.dump(pajamos, file)
with open("Islaidos.pickle", mode="wb") as file:
    # noinspection PyTypeChecker
    pickle.dump(islaidos, file)
