# Materia: Programacion I
# Entrega de la Unidad 4 - Estructuras Repetitivas
# Alumno: Julio Roja
# Comision: 20

import random
import math

# EJERCICIO 1
for x in range(1, 101):
    print(x)

# EJERCICIO 2
num = int(input("Ingrese un número: "))
contador = 0
while num > 0:
    num //= 10
    contador += 1
print(f"La cantidad de dígitos es: {contador}")

# EJERCICIO 3
primer_num = int(input("Ingrese un número: "))
segundo_num = int(input("Ingrese un número: "))
resultado = 0

if primer_num > segundo_num:
    print("El primer número debe ser menor que el segundo.")
else:
    for i in range(primer_num + 1, segundo_num):
        resultado += i
    print("El resultado es", resultado)

# EJERCICIO 4
num = int(input("Ingrese un número o 0 para terminar: "))
suma = 0
while num != 0:
    suma += num
    num = int(input("Ingrese un número o 0 para terminar: "))
print("La suma de los números ingresados es:", suma)

# EJERCICIO 5
intentos = 1
numero_secreto = random.randint(0, 9)
num = int(input("Ingrese un número entre 0 y 9: "))
while num != numero_secreto:
    intentos += 1
    print("No es correcto. Intenta nuevamente.")
    num = int(input("Ingrese un número entre 0 y 9: "))
print(f"¡Felicidades! Adivinaste el número secreto en {intentos} intentos.")

# EJERCICIO 6
for i in range(100, 0, -1):
    print(i)

# EJERCICIO 7
num = int(input("Ingrese un número: "))
if num > 0:
    for i in range(0, num + 1):
        print(i)
else:
    print("El numero debe ser positivo")

# EJERCICIO 8
ciclos = 100
par = 0
impar = 0
positivo = 0
negativo = 0
for i in range(ciclos):
    numeros = int(input("Ingrese un número: "))
    if numeros % 2 == 0:
        par += 1
    else:
        impar += 1

    if numeros > 0:
        positivo += 1
    elif numeros < 0:
        negativo += 1
print(f"Cantidad de números pares: {par}")
print(f"Cantidad de números impares: {impar}")
print(f"Cantidad de números positivos: {positivo}")
print(f"Cantidad de números negativos: {negativo}")

# EJERCICIO 9
ciclos = 100
resultado = 0
for i in range(ciclos):
    num = int(input("Ingrese un número: "))
    resultado += num
print(f"La media de los números ingresados es: {resultado / ciclos}")

# EJERCICIO 10
num = int(input("Ingrese un número: "))
invertido = 0
while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num = num // 10
print(f"El número invertido es: {invertido}")
