import pickle

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


while True:
    print("Sveiki atvykę į minibiudžetio programą\n"
          "Pagrindinis meniu\n"
          "1 - Įvesti pajamas\n"
          "2 - Įvesti išlaidas\n"
          "3 - Atspausdinti pajamų eilutes\n"
          "4 - Atspausdinti išlaidų eilutes\n"
          "5 - Atspausdinti statistiką\n"
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
