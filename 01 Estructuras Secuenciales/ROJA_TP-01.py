# Materia: Programacion I
# Entrega de la Unidad 1 - Estructuras Secuenciales
# Alumno: Julio Roja
# Comision: 20

# EJERCICIO 1
print("Hola Mundo!")


# EJERCICIO 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")


# EJERCICIO 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# EJERCICIO 4
radio = float(input("Ingrese el radio de un circulo: "))
area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio

print(f"El area es {area}")
print(f"El perimetro es {perimetro}")


# EJERCICIO 5
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600

print(f"El equivalente en horas es: {horas}")


# EJERCICIO 6
numero = int(input("Ingrese un numero: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {i*numero}")


# EJERCICIO 7
num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))

if num1 == 0 or num2 == 0:
    print("El numero no puede ser 0")
else:
    print(f"La suma de {num1} y {num2} es {num1 + num2}")
    print(f"La resta de {num1} y {num2} es {num1 - num2}")
    print(f"La multiplicacion de {num1} y {num2} es {num1 * num2}")
    print(f"La division de {num1} y {num2} es {num1 / num2}")


# EJERCICIO 8
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

print(f"Tu indice de masa corporal es: {imc}")


# EJERCICIO 9
celcius = float(input("Ingrese grados Celsius: "))
fahrenheit = celcius * 1.8 + 32

print(f"{celcius}°C equivalen a {fahrenheit}°F")


# EJERCICIO 10
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio es {promedio}")
