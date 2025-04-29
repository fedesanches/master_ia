""" Listas por comprehension """

a = [1, 2, 3, 4, 5]
b = [2 * x for x in a]

print(b)


datos = [{"nombre": "Matías", "equipo": "Boca"},
     {"nombre": "Daniela", "equipo": "Racing"},
     {"nombre": "Francisco", "equipo": "San Lorenzo"}]

nombres = [d["nombre"] for d in datos]
print(nombres)


a = [1, 2, 3, 4, 5]
b = [2 * x for x in a if x > 3]
print(b)

b = [2 * x if x > 3 else x for x in a]
print(b)


productos = [
    {"nombre": "Harina", "cantidad": 4, "precio_unitario": 0.75},
    {"nombre": "Muzarela", "cantidad": 3, "precio_unitario": 1.0},
    {"nombre": "Salsa de tomate", "cantidad": 3, "precio_unitario": 1.5},
    {"nombre": "Aceitunas", "cantidad": 2, "precio_unitario": 1.25},
    {"nombre": "Levadura", "cantidad": 1, "precio_unitario": 0.4},
]

a = [p for p in productos if p["precio_unitario"] >= 1 and p["cantidad"] > 2]
print(a)

b = sum([p["cantidad"] * p["precio_unitario"] for p in productos])
print(b)

c = max([p["cantidad"] for p in productos])
print(c)

""" "obtener el producto que mas unidades se vendio" """

d = [p for p in productos if p["nombre"] in ["Harina", "Aceitunas"]]
print(d)

e = [(p["nombre"], p["precio_unitario"]) for p in productos]
print(e)

f = {p["nombre"]: p["precio_unitario"] for p in productos}
print(f)


lista_compuesta = [[0, 2, 4], [5, 6], [7, 8, 9, 10]]

lista_aplanada = [x for sublista in lista_compuesta for x in sublista]
print(lista_aplanada)

lista_aplanada_de_listas_grandes = [x for sublista in lista_compuesta
                                        for x in sublista if len(sublista) > 2]
print(lista_aplanada_de_listas_grandes)



""" Clases """
class Estudiante():

    def __init__(self, _nombre, _apellido, _edad):
        self.nombre = _nombre
        self.apellido = _apellido
        self.edad = _edad
        
    def imprimir(self):
        print(f"{self.nombre} {self.apellido} ({self.edad})")
        
    def cumplir_anos(self):
        self.edad += 1
    

est_1 = Estudiante("Juan", "Hola", 3)
print(est_1.nombre)

est_1.nombre = "Ruperto"
print(est_1.nombre)

est_1.imprimir()

est_1.cumplir_anos()
print(est_1.edad)


class EstudianteUdesa(Estudiante):
    def __init__(self, _nombre, _apellido, _edad, _usuario):
        super().__init__(_nombre, _apellido, _edad)
        self.usuario = _usuario
    
    def imprimir(self):
        super().imprimir()
        print(f"Usuario: {self.usuario}")

est_2 = EstudianteUdesa("Juan", "Hola", 3, "algo")
est_2.imprimir()