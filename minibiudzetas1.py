

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
    if pasirinkimas == "q":
        print("Išėjote iš programos")
        break
