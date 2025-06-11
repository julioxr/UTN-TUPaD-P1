# Materia: Programacion I
# Entrega de la Unidad 6 - Recursividad
# Alumno: Julio Roja
# Comision: 20

# EJERCICIO 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


limite = int(input("Ingrese un número entero positivo: "))

for i in range(1, limite + 1):
    print(f"{i} != {factorial(i)}")


# EJERCICIO 2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


limite = int(input("Cuantos terminos de la serie de Fibonacci querés ver? "))

for i in range(limite):
    print(f"Fibonacci({i}) = {fibonacci(i)}")


# EJERCICIO 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")


# EJERCICIO 4
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


numero = int(input("Ingrese un número entero positivo: "))
binario = decimal_a_binario(numero)
if binario == "":
    binario = "0"
print(f"El número {numero} en binario es {binario}")


# EJERCICIO 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


print(es_palindromo("neuquen"))
print(es_palindromo("reconocer"))
print(es_palindromo("perro"))


# EJERCICIO 6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)


print(suma_digitos(1234))
print(suma_digitos(9))
print(suma_digitos(305))


# EJERCICIO 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


print(contar_bloques(1))
print(contar_bloques(2))
print(contar_bloques(4))


# EJERCICIO 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)


print(contar_digito(12233421, 2))
print(contar_digito(5555, 5))
print(contar_digito(123456, 7))
