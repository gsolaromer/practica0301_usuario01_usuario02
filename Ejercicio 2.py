import csv
import cProfile

def capitalizar_nombre(nombre):
    '''Función que capitaliza el nombre.
    
    Parámetros:
        - Nombre.
    Salida:
        - Nombre capitalizado.
    '''
    return nombre.capitalize()

def calcular_letra_dni(dni):
    '''Función que calcula la letra del DNI.
    
    Parámetros:
        - Número de DNI.
    Salida:
        - Letra de número de DNI.
    '''
    letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
    dni_numero = int(dni) % 23
    return letras[dni_numero]

def procesar_datos(ruta_1, ruta_2):
    '''Función que lee dos ficheros csv con una 
    lista larga de datos de personas (50 personas y 1000 personas) 
    y llama a dos funciones que pongan su nombre en formato capitalizado 
    y calculen la letra de DNI correspondiente.
    
    Parámetros:
        - Fichero 50.csv
        - Fichero 1000.csv

    Salida:
        - lista_1: Lista con los datos del primer archivo.
        - lista_2: Lista con los datos del segundo archivo.
    '''

    lista_1 = []
    with open(ruta_1, newline='', encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile)
        for fila in reader:
            nombre = capitalizar_nombre(fila[0].strip())
            dni = calcular_letra_dni(fila[1].strip())
            lista_1.append((nombre, dni))

    lista_2 = []
    with open(ruta_2, newline='', encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile)
        for fila in reader:
            nombre = capitalizar_nombre(fila[0].strip())
            dni = calcular_letra_dni(fila[1].strip())
            lista_2.append((nombre, dni))
    
    return lista_1, lista_2

ruta_1 = "C:\\Users\\gabri\\Escritorio\\GIT_gsolaromerEduca\\practica0301_usuario01_usuario02\\50.csv"
ruta_2 = "C:\\Users\\gabri\\Escritorio\\GIT_gsolaromerEduca\\practica0301_usuario01_usuario02\\1000.csv"

lista_1, lista_2 = procesar_datos(ruta_1, ruta_2)

print()
for nombre, dni in lista_1:
    print(nombre,dni)

print()
for nombre, dni in lista_2:
    print(nombre,dni)

cProfile.run("procesar_datos(ruta_1, ruta_2)")