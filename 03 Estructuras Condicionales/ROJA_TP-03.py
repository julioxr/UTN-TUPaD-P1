# Materia: Programacion I
# Entrega de la Unidad 3 - Estructuras Condicionales
# Alumno: Julio Roja
# Comision: 20

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
