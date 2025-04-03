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

# EJERCICIO 7
frase = input("Ingrese una palabra o frase: ")
ultima_letra = frase[-1].lower()
if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(f"{frase}!")
else:
    print(frase)

# EJERCICIO 8
nombre = input("Ingrese su nombre: ")
print("1. Convertir nombre a mayusculas")
print("2. Convertir nombre a minusculas")
print("3. Convertir la prigit mera letra a mayuscula")
opcion = int(input("Ingrese la opcion deseada: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

# EJERCICIO 9
magnitud = float(input("Ingrese la magnitud del sismo: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
elif magnitud >= 7:
    print("Extremo")
