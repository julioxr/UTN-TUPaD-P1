# Materia: Programacion I
# Entrega de la Unidad 5 - Funciones
# Alumno: Julio Roja
# Comision: 20

# EJERCICIO 1
def imprimir_hola_mundo():
    print("Hola Mundo")


# EJERCICIO 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")


# EJERCICIO 3
def informacin_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# EJERCICIO 4
def calcular_area_circulo(radio):
    area = 3.14 * radio ** 2
    print(f"El area del circulo es: {area}")
    return area


def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    print(f"El perimetro del circulo es: {perimetro}")
    return perimetro


# EJERCICIO 5
def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} segundos son {horas} horas.")


# EJERCICIO 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


# EJERCICIO 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    tupla_resultados = (suma, resta, multiplicacion, division)
    print(tupla_resultados)


# EJERCICIO 8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Tu IMC es: {imc:.2f}")
    return imc


# EJERCICIO 9
def celcius_a_fahrenheit(grados_celcius):
    temp_celsius = grados_celcius
    grados_fahrenheit = (grados_celcius * 9/5) + 32
    print(f"{temp_celsius}°C equivale a {grados_fahrenheit:.2f}°F")


# EJERCICIO 10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio es: {promedio:.2f}")
    return promedio


# Programa principal
imprimir_hola_mundo()
saludar_usuario("Julio")
informacin_personal("Julio", "Roja", 37, "Buenos Aires")
calcular_area_circulo(5)
calcular_perimetro_circulo(5)
segundos_a_horas(3600)
tabla_multiplicar(7)
operaciones_basicas(6, 4)
calcular_imc(70, 1.75)
celcius_a_fahrenheit(45)
calcular_promedio(10, 20, 30)
