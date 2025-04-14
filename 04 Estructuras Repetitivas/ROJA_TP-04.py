# Materia: Programacion I
# Entrega de la Unidad 4 - Estructuras Repetitivas
# Alumno: Julio Roja
# Comision: 20

import random

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


# EJERCICIO 7

# EJERCICIO 8

# EJERCICIO 9

# EJERCICIO 10
