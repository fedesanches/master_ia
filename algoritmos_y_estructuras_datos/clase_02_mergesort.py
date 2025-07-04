import sys
import time
import random
import matplotlib.pyplot as plt

def merge_sort(a):
    # COMPLETAR
    if len(a) <= 1: 
        return a
    
    len_split = len(a) // 2
    left_part = a[:len_split]
    right_part = a[len_split:]
    
    left_part = merge_sort(left_part)
    right_part = merge_sort(right_part)
    
    merge = []
    i, j = 0, 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            merge.append(left_part[i])
            i += 1
        else:
            merge.append(right_part[j])
            j += 1
            
    while i < len(left_part):
        merge.append(left_part[i])
        i += 1

    while j < len(right_part):
        merge.append(right_part[j])
        j += 1
    
    a = merge
    return a

#### Casos de test

def permutaciones(a):
    if len(a) == 0:
        yield []
        return
    for i in range(len(a)):
        for p in permutaciones(a[1:]):
            yield p[:i] + [a[0]] + p[i:]

def casos_de_test():
    for i in range(8):
        for lista in permutaciones(list(range(i))):
            yield lista
    yield list(range(1000)) 
    yield list(reversed(range(1000)))
    for i in range(100):
        yield [random.randrange(100) for _ in range(100)]

def testear_sobre_entrada(algoritmo, lista):
    lista_ordenada = algoritmo(lista[:])
    if lista_ordenada == sorted(lista):
        return True
    sys.stderr.write('Error en el algoritmo implementado:\n')
    sys.stderr.write(f'Entrada: {lista}\n')
    sys.stderr.write(f'Salida esperada: {sorted(lista)}\n')
    sys.stderr.write(f'Salida devuelta: {lista}\n')
    return False

def testear(algoritmo):
    casos = list(casos_de_test())
    total = len(casos)
    correctos = 0
    for i in range(len(casos)):
        lista = casos[i]
        print(f'Test {i}/{total}.')
        if testear_sobre_entrada(algoritmo, lista):
            correctos += 1
        else:
            break
    if correctos == total:
        print(f'Todos los tests OK ({correctos}/{total}).')
        return True
    else:
        print(f'Fallan algunos tests. Pasan {correctos}/{total}.')
        return False

#### Comparación de tiempos

def selection_sort(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a

def comparar_tiempos(tamanio):
    benchmarks = []
    for k in range(tamanio):
        benchmarks.append([random.randrange(tamanio) for _ in range(k)])
    t_selection_sort = []
    t_merge_sort = []
    for entrada in benchmarks:
        # Medir tiempo de selection sort
        t0 = time.time()
        selection_sort(entrada[:])
        t1 = time.time()
        t_selection_sort.append(t1 - t0)
        # Medir tiempo de merge sort
        t0 = time.time()
        merge_sort(entrada[:])
        t1 = time.time()
        t_merge_sort.append(t1 - t0)
    # Graficar
    plt.plot(range(tamanio), t_merge_sort, "-b", label='merge sort')
    plt.plot(range(tamanio), t_selection_sort, "-r", label='selection sort')
    plt.legend(loc='upper left')
    plt.xlabel("Tamaño de la entrada")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Comparación de selection sort vs. merge sort")
    plt.show()

#### Principal: testear y comparar tiempos

def main():
    print('*** Corriendo tests sobre merge sort')
    if not testear(merge_sort):
        print('!!! El algoritmo no supera los tests.')
        sys.exit(1)
    print('*** Comparando tiempos de selection sort vs. merge sort')
    comparar_tiempos(tamanio=500)

if __name__ == '__main__':
    main()

