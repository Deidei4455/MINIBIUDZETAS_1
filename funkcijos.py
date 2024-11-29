# didžiausios išlaidos arba max atlyginimas
def gauk_maximuma(listas):
    """
    Funkcija priima listą ir suranda didžiausią skaičių
    tame liste, kuris yra liste,
    pvz. kaip atlyginimas didžiausias, grąžina
    didžiausią skaičių kaip rezultatą.
    :param listas: list
    :return: max
    """
    skaiciai = []
    maximum = []
    for vard, pareig, atlg in listas:
        skaiciai.append(atlg)
    for elem in listas:
        if max(skaiciai) in elem:
            maximum.append(elem)

    return maximum


# listuose esamų pajamų arba išlaidų suma

def gauk_bendra_suma(listas):
    """
    funkcija priima listą ir gražina
    skaičių sumą.
    :param listas: list
    :return: suma
    """
    suma = 0
    for elem in listas:
        suma += elem[2]
    return suma


# mažiausiai uždirbantis-(ys)
def gauk_minimuma(listas):
    """
    funkcija priima listą ir grąžina
    mažiausią skaičių listo liste.
    :param listas: list
    :return: minimumas
    """
    atlyginimai = []
    minimum = []
    for vard, pareig, atlg in listas:
        atlyginimai.append(atlg)
    for elem in listas:
        if min(atlyginimai) in elem:
            minimum.append(elem)

    return minimum


# vidurkio apskaičiavimas


def gauk_vidurki(listas):
    """
    funkcija priima sudėtinį listą ir grąžina
    to listo skaičių vidurkį kaip rezultatą.
    :param listas: list
    :return: vidurkis
    """
    suma = 0
    for elem in listas:
        suma += elem[2]
    avg = suma / len(listas)
    return avg
