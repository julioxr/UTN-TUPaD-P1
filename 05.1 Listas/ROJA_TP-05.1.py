# Materia: Programacion I
# Entrega de la Unidad 5.1 - Listas
# Alumno: Julio Roja
# Comision: 20

# EJERCICIO 1
lista = list(range(1, 100, 4))
print(lista)

# EJERCICIO 2
lista = [True, 15, "hola", 3.1, 8]
print(lista[-2])

# EJERCICIO 3
lista_vacia = []
lista_vacia.append(1)
lista_vacia.append(2)
lista_vacia.append("hola")
print(lista_vacia)

# EJERCICIO 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"

print(animales)

# EJERCICIO 5
# Lo que hace el siguiente programa es eliminar el mayor de los numeros de la lista "numeros"
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# EJERCICIO 6
lista = list(range(10, 31, 5))
print(lista[0:2])

# EJERCICIO 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "coupe"]
print(autos)

# EJERCICIO 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

# EJERCICIO 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = ("tallarines")
compras[0].remove("pan")

print(compras)

# EJERCICIO 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)

# Programa principal
