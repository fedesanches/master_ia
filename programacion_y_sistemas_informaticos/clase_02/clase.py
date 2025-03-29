'''
nombres = ['1', '2', '3']

for e in enumerate(nombres): print(e)

for nombre in nombres: nombres.index('1')

nombres.remove('2')
print(nombres)

nombres.sort(reverse=True)
print(nombres)

nombres.append('hola')
print(nombres)

for x in range(len(nombres)) : print(nombres[x])
'''

a = [1,2,3]
b = 2
c = 'Hola Matias'
b = a 
'''
es una referencia a la lista de a; no es una copia
'''
e = a.copy()

def agregar_un_dos(l):
    l.append(2)
    return l

d = agregar_un_dos(a)

print(f'a vale {a}')
print(f'b vale {b}')
print(f'c vale {c}')
print(f'd vale {d}')



import csv

f = open('productos.csv')
'''
rows = csv.reader(f)
headers = next(rows)
print(headers)

for row in rows:
    print(row)
'''

precios = {}

with open('productos.csv', 'r') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        print(row)
        precios[row[0]] = float(row[3])

print(precios)
    

f.close()