""" Ejercicio 1 """
class VectorConUndo():

    def __init__(self, n):
        self._datos = [0 for i in range(n)]
        self._ultima_posicion = None
        self._ultimo_valor = None

    def leer(self, i):
        return self._datos[i]
    
    def escribir(self, i, x):
        # Guardo la ultima posicion que cambie y cual fue su valor; esto no afecta la complejidad la cual sigue siendo O(1)
        self._ultima_posicion = i
        self._ultimo_valor = self._datos[i]
        self._datos[i] = x
    
    def ctrlZ(self):
        if self._ultimo_valor is None and self._ultima_posicion is None:
            return None
        else:
            self._datos[self._ultima_posicion] = self._ultimo_valor

# La invariante es para el vector es siempre de tamaño "n", _ultima_posicion es None o un valor entre 0-n y _ultimo_valor es None o el valor del vector en la posicion "_ultima_posicion"

""" Ejercicio 2 """
def exponenciacionBinaria(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = exponenciacionBinaria(x, n // 2)
        return y * y
    else:
        y = exponenciacionBinaria(x, (n - 1) // 2)
        return y * y * x

# Casos de test
assert exponenciacionBinaria(10, 2) == 100
assert exponenciacionBinaria(5, 6) == 15625
assert exponenciacionBinaria(0, 10) == 0
assert exponenciacionBinaria(10, 0) == 1

# La complejidad temporal la exponenciacion binaria es O(log n); ya que cada iteracion implica ir hacia la mitad del exponente.

""" Ejercicio 3 """
class Nodo:
    def __init__(self, left, value, right):
        self.left = left
        self.value = value
        self.right = right

def avl(arreglo):
    if not arreglo: return None
    
    raiz = arreglo[len(arreglo) // 2]
    left_array = arreglo[:len(arreglo) // 2]
    right_array = arreglo[(len(arreglo) // 2) + 1:]
    
    arbol = Nodo(None, raiz, None)
    arbol.left = avl(left_array)
    arbol.right = avl(right_array)
    
    return arbol