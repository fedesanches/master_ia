import csv
from collections import Counter

def arboles_parque(nombre_archivo, nombre_parque):
    arboles = {}

    with open(nombre_archivo, 'r', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['espacio_ve'] == nombre_parque:
                arboles[reader.line_num] = row
                
    return arboles


def arbol_mas_popular(nombre_parque):
    arboles = arboles_parque('arbolado-en-espacios-verdes.csv', nombre_parque)
    arboles_nombres = []

    for arbol in arboles.values():
        arboles_nombres.append(arbol['nombre_com'])

    return Counter(arboles_nombres).most_common(1)[0][0]


def n_mas_altos(nombre_parque, n):
    arboles = arboles_parque('arbolado-en-espacios-verdes.csv', nombre_parque)
    arboles_altos = dict(sorted(arboles.items(), key=lambda x: float(x[1]['altura_tot']), reverse=True)[:n])
    return arboles_altos


def altura_promedio(nombre_parque, especie):
    arboles = arboles_parque('arbolado-en-espacios-verdes.csv', nombre_parque)
    alturas = []

    for arbol in arboles.values():
        if arbol['nombre_com'] == especie:
            alturas.append(float(arbol['altura_tot']))

    return sum(alturas) / len(alturas)


def cantidad_de_arboles(nombre_parque):
    arboles = arboles_parque('arbolado-en-espacios-verdes.csv', nombre_parque)
    return len(arboles)






#print(arbol_mas_popular('CENTENARIO'))
#print(n_mas_altos('CENTENARIO', 5))
print(cantidad_de_arboles('CENTENARIO'))