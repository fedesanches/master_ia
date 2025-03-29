def invertir_lista(lista):
    return lista.sort(reverse=True)

a = [1, 2, 3, 4, 5]
b = ['Bogotá', 'Rosario', 'San Fernando', 'San Miguel']

invertir_lista(a)
print(a)

invertir_lista(b)
print(b)