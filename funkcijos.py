# didžiausios išlaidos arba max atlyginimas
def maximumas(listas):
    atlyginimai = []
    maximum = []
    for vard, pareig, atlg in listas:
        atlyginimai.append(atlg)
    for elem in listas:
        if max(atlyginimai) in elem:
            maximum.append(elem)

    return maximum


# listuose esamų pajamų arba išlaidų suma

def sumuok(listas):
    suma = 0
    for elem in listas:
        suma += elem[2]
    return suma


# mažiausiai uždirbantis-(ys)
def minimumas(listas):
    atlyginimai = []
    minimum = []
    for vard, pareig, atlg in listas:
        atlyginimai.append(atlg)
    for elem in listas:
        if min(atlyginimai) in elem:
            minimum.append(elem)

    return minimum


# vidurkio apskaičiavimas


def vidurkis(listas):
    suma = 0
    for elem in listas:
        suma += elem[2]
    avg = suma / len(listas)
    return avg
