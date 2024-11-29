import pickle
import funkcijos

try:
    with open("MINIBIUDŽETAS_1.pickle", mode="rb") as file:
        pajamos_islaidos = pickle.load(file)
except FileNotFoundError:
    pajamos_islaidos = [[], []]

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
        pajamos_islaidos[0].append(pajamu_tipas)
        print(f"Įvestos pajamos {pajamu_tipas}")
        input("Tęskite su enter ")
    elif pasirinkimas == "2":
        data_islaidos = input("Įveskite išlaidų datą: ")
        islaidu_name = input("Įveskite išlaidų pavadinimą (maistas, būstas ...): ")
        islaidu_suma = int(input("Įveskite išlaidų sumą: "))
        islaidu_tipas = [data_islaidos, islaidu_name, islaidu_suma]
        pajamos_islaidos[1].append(islaidu_tipas)
        print(f"Įvestos išlaidos {islaidu_tipas}")
        input("Tęskite su enter ")
    elif pasirinkimas == "3":
        for elem in pajamos_islaidos[0]:
            print(f"data: {elem[0]}, pajamų tipas: {elem[1]}, {elem[2]}")
        input("Tęskite su enter ")
    elif pasirinkimas == "4":
        for elem in pajamos_islaidos[1]:
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
                eilutes_max = funkcijos.gauk_maximuma(pajamos_islaidos[0])
                eilutes_min = funkcijos.gauk_minimuma(pajamos_islaidos[0])
                eilutes_suma = funkcijos.gauk_bendra_suma(pajamos_islaidos[0])
                eilutes_avg = funkcijos.gauk_vidurki(pajamos_islaidos[0])
                for elem in eilutes_max:
                    print(f"Didžiausios pajamos, data: {elem[0]}. {elem[1]}: {elem[2]}")
                for elem in eilutes_min:
                    print(f"Mažiausios pajamos, data: {elem[0]}. {elem[1]}: {elem[2]}")
                print(f"Visų pajamų suma - {eilutes_suma}")
                print(f"Visų pajamų vidurkis - {eilutes_avg}")
                input()
            elif Statistikos_pasirinkimas == "2":
                islaidos_max = funkcijos.gauk_maximuma(pajamos_islaidos[1])
                islaidos_min = funkcijos.gauk_minimuma(pajamos_islaidos[1])
                islaidos_suma = funkcijos.gauk_bendra_suma(pajamos_islaidos[1])
                islaidos_avg = funkcijos.gauk_vidurki(pajamos_islaidos[1])
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
                for elem in enumerate(pajamos_islaidos[0]):
                    print(elem)
                indeksas = int(input("Įveskite skaičių, indeksuojantį, kurias pajamas pašalinti: "))
                pajamos_islaidos[0].remove(pajamos_islaidos[0][indeksas])
                print(pajamos_islaidos[0])
                input()
            elif Trynimo_pasirinkimas == "2":
                for elem in enumerate(pajamos_islaidos[1]):
                    print(elem)
                indeksas = int(input("Įveskite skaičių, indeksuojantį, kurias išlaidas pašalinti: "))
                pajamos_islaidos[1].remove(pajamos_islaidos[1][indeksas])
                print(pajamos_islaidos[1])
                input()
            elif Trynimo_pasirinkimas == "q":
                break
    elif pasirinkimas == "7":
        while True:
            print("Įveskite raktažodį, ką norite surasti (pvz. stipendija, maistas ...)\n"
                  "arba 'q' Eiti atgal")
            Paieska_pasirinkimas = input("> ")
            if Paieska_pasirinkimas == "q":
                break
            for elem in pajamos_islaidos[0]:
                if Paieska_pasirinkimas in elem:
                    print(elem[0], elem[1], elem[2])

            for elem in pajamos_islaidos[1]:
                if Paieska_pasirinkimas in elem:
                    print(elem[0], elem[1], elem[2])

            input("Tęskite su enter ")
    elif pasirinkimas == "q":
        print("Išėjote iš programos")
        break

print(pajamos_islaidos)

with open("MINIBIUDŽETAS_1.pickle", mode="wb") as file:
    # noinspection PyTypeChecker
    pickle.dump(pajamos_islaidos, file)
