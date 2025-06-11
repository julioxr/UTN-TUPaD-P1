# Materia: Programacion I
# Entrega de la Unidad 7 - Datos Complejos
# Alumno: Julio Roja
# Comision: 20

# EJERCICIO 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# EJERCICIO 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# EJERCICIO 3
solo_frutas = list(precios_frutas.keys())
print(solo_frutas)

# EJERCICIO 4
contactos = {}
for _ in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    contactos[nombre] = numero

consulta = input("Ingrese el nombre a consultar: ")
if consulta in contactos:
    print(f"El número de {consulta} es {contactos[consulta]}")
else:
    print("Contacto no encontrado.")

# EJERCICIO 5
frase = input("Ingrese una frase: ")
palabras = frase.split()
unicas = set(palabras)
print("Palabras únicas:", unicas)

conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1
print("Repeticiones de cada palabra:", conteo)


# EJERCICIO 6
alumnos = {}
for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese nota {i+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {promedio:.2f}")


# EJERCICIO 7
parcial1 = {1, 2, 3, 4}
parcial2 = {3, 4, 5, 6}

ambos = parcial1 & parcial2
print("Aprobaron ambos:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)


# EJERCICIO 8
stock = {}

producto = input("Producto a consultar o agregar: ")
if producto in stock:
    agregar = int(input("¿Cuántas unidades agregar? "))
    stock[producto] += agregar
else:
    stock[producto] = int(
        input("Ingrese cantidad inicial para este producto: "))

print(stock)

# EJERCICIO 9
agenda = {}
agenda[("lunes", "10:00")] = "Reunión"
agenda[("martes", "15:00")] = "Examen"

dia = input("Ingrese día: ")
hora = input("Ingrese hora (formato HH:MM): ")
clave = (dia, hora)
if clave in agenda:
    print(f"Actividad: {agenda[clave]}")
else:
    print("No hay actividad agendada para ese día y hora.")


# EJERCICIO 10
paises_capitales = {'Argentina': 'Buenos Aires',
                    'Chile': 'Santiago', 'Uruguay': 'Montevideo'}
capitales_paises = {capital: pais for pais,
                    capital in paises_capitales.items()}

print(capitales_paises)
