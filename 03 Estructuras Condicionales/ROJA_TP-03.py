# Materia: Programacion I
# Entrega de la Unidad 3 - Estructuras Condicionales
# Alumno: Julio Roja
# Comision: 20

import random
from statistics import mode, median, mean

# EJERCICIO 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

# EJERCICIO 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# EJERCICIO 3
numero = int(input("Ingrese un numero par: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

# EJERCICIO 4
edad = int(input("Ingrese su edad: "))
if edad > 0 and edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")

# EJERCICIO 5
contrasena = input("Ingrese la contraseña: ")
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# EJERCICIO 6
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No hay sesgo claro")
