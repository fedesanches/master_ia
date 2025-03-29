dic = {'Cuaderno': ['15.0'], 
       'Lapiz': ['1.2', '20'], 
       'Goma': ['0.8'], 
       'Resaltador': ['3.5', '3.5', '3.5'],
       'Lapicera': ['3.5', '3.5', '3.5']
}

def contar_definiciones(d):
    new_dict = {}
    for key in d:
        new_dict[key] = len(d[key])
        
    return print(new_dict)


def cantidad_de_claves_letra(d, l):
    c = 0
    for key in d:
        if key[:1].upper() == l.upper(): c += 1
    return print(c)


contar_definiciones(dic)
cantidad_de_claves_letra(dic, 'L')