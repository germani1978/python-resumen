# DOCUMENTACIÓN
# docs.python.org/es


# 0 consola
# El comando py para entrar al compilador de Python funciona en Windows.
# En sistemas Unix, puedes usar python en lugar de py.
# cls - Borrar consola:
# cd .. - Salir del directorio
# mkdir - Crear directorio
# cd - Entrar al directorio
# ls - Listar directorios
# touch - Crear archivo. touch mi_archivo.txt
# echo. > mi_archivo.txt
# py - Entrar al compilador de Python (solo en Windows)
# pip freeze    #dice los módulos que hay instalado
# pip install pandas #instalar un modulo de python
# pip freeze > requirements.txt #copia el resultado en el archivo requirements.txt
# pip install -r requirements.txt #instala los modulos que hay en el archivo


# 1 Variables y Operadores
x = 10
LIMITE = 1000  # constante
cadena = "Hola, mundo"
type(cadena)
parrafo = """
Esto es un parrafo
Aqui se puede escribir muchas cosas.
Con muchas lineas
"""
# 5 / 2 = 2.5
# 5 // 2 = 2
# 5 % 2 = 1 #resto de la división
# 3 ** 2 = 9 #potencia
# cadena*2 = "Hola, mundoHola, mundo"
float(3)  # convierte a decimales
str(43)  # convierte a string
round(434.3456, 2)  # redondea 2 numeros después de la coma
# int(23.5) convertir a entero
pass  # para rellenar instrucciones


# 2 cadenas
# Cadena en mayúscula
texto = "Hola, mundo!"
mayusculas = texto.upper()  # Convierte el texto a mayúsculas

# Primera letra en mayúscula
nombre = "juan"
capitalizado = nombre.capitalize()  # Capitaliza la primera letra

# Quitar espacios basura al principio o al final
cadena = "   Esto es una cadena con espacios   "
sin_espacios = cadena.strip()  # Elimina espacios al principio y al final

# Pasar a minúsculas
texto = "TEXTO EN MINÚSCULAS"
minusculas = texto.lower()  # Convierte a minúsculas

# Reemplazar todas las letras 'o' por 'a'
frase = "Hola, cómo estás?"
reemplazado = frase.replace("o", "a")  # Reemplaza 'o' con 'a'

# Primer caracter
palabra = "Python"
primer_caracter = palabra[0]  # Obtiene el primer caracter


# 3 input
print("Hola " + input("Cual es tu nombre?"))


# 4 Listas y tuplas
lista = [1, 2, 3, 4]
len(lista)
lista.append(1)
lista.pop(2)
"".join(lista)  # devuelve un string
lista[1:3]  # [2, 3]
max(lista)  # 5
min(lista)  # 1
lista_tupla = (1, 2, 3, 4)


# 5 diccionarios
dict = {"casa": "edificación para vivir"}
dict["casa"]  # "edificación para vivir"
for item in dict.keys():
    print(item)
for item in dict.values():
    print(item)
for llave, valor in dict.items():
    print(valor)
    print(llave)


# 6 control de flujo y ciclos
if 3 < 4:
    print("La condición es verdadera")
else:
    print("La condicion es falsa")

for x in [1, 2, 3, 4]:
    print(x)

for i in range(1, 1001):
    print(i)

while x > 2:
    x = 3

for letra in nombre:
    print(letra)


# 7 random
import random

x = random.randint(1, 100)
random.choice(lista)


# 8 funciones
def saluda(nombre, edad):
    print("Hola, " + nombre)


fu = lambda x: x**2  # es como f(x)


def add(*arg):
    print(arg)  # 2,3,4


add(2, 3, 4)


def add(**kwargs):  # kwargs es un dicionario
    print(kwargs)  # {'add': 4, 'peso': 50}
    print(kwargs["add"])  # 4


add(add=4, peso=50)


def saludo(func):  # funcion superior
    func()


# 9 clases
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Labrador(Perro):  # herencia
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color


class Car:
    def __init__(self, **kw):
        self.model = kw["model"]


my_car = Car(model="ferrari")


class Car:
    def __init__(self, **kw):
        # self.model = kw['model']        # este es igual que el de abajo
        self.model = kw.get("model")  # pero este si no esta 'model' no da error


my_car = Car(model="Ferrari")
print(my_car.model)


# 10 map
def cuadrado(x):
    return x**2


cuadrados = list(map(cuadrado, [1, 2, 3, 4, 5]))  # 1,4,9,16,81


# 11 filter
def es_par(x):
    return x % 2 == 0


pares = list(filter(es_par, [1, 2, 3, 4, 5]))  # 2,4


# 12 reducer
from functools import reduce


def suma(x, y):
    return x + y


suma_total = reduce(suma, [1, 2, 3, 4, 5], 0)


# 13 enumarate
for index, x in enumerate([3, 6, 7]):
    print(index, x)
# 0 3
# 1 6
# 2 7


# 14 zip
for x, y in zip([1, 2, 3], [4, 5, 6]):
    print(x, y)
# 1 4
# 2 5
# 3 6


# 15 Scope
x = 1


def fun():
    global x  # es mejor usar return
    x += 1
    print(x)  # 2


fun()


# 16 Excepciones
try:
    division = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Esto siempre se imprime")


# 17 archivos
with open("archivo.txt", "w") as f:
    f.write("Hola, mundo")
    f.close()

with open("archivo.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)


# 18 Comprensiones de Listas y Diccionarios
numeros = [1, 2, 3]
new = [2 * n for n in numeros]
a = [i**2 for i in range(1, 100) if i % 3 != 0]
a = {i**2 for i in range(1, 100) if i % 3 != 0}
names = ["Juan", "Pedro", "Susana", "Luis"]
puntuacion = {
    name: random.radint(1, 100) for name in names
}  # {'Juan': 31, 'Pedro': 53, 'Susana': 87, 'Luis': 16}
students = {
    student: score for (student, score) in puntuacion.items() if score > 60
}  # {'Susana': 87}


# 19 generadores
def generador(n):  # 1,2,3..n
    for i in range(n):
        yield i


# 20 Decoradores
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])

    return wrapper


# 21 Expresiones Regulares:
import re

patron = r"\d+"
coincidencia = re.search(patron, "Este texto contiene un número: 42")


# 22 importar
import math  # modulo
from math import sqrt  # paquete


# 23 Manejo de fechas y horas
import datetime

fecha = datetime.datetime.now()


# 24 csv
import csv

with open("./data.csv", "r") as file:
    data = csv.reader(file)
    for row in data:
        print(row)


# 25 Manejo de archivos JSON
import json

with open("datos.json", "r") as f:
    datos = json.load(f)


# 26 base de datos
import mysql.connector

# Establecer la conexión
cnx = mysql.connector.connect(
    host="localhost",
    user="mi_usuario",
    password="mi_contraseña",
    database="mi_base_de_datos",
)

# Crear un cursor para realizar consultas
cursor = cnx.cursor()

# Ejecutar una consulta SELECT
query = "SELECT * FROM mi_tabla"
cursor.execute(query)

# Recorrer y mostrar los resultados
for fila in cursor.fetchall():
    print(fila)

# inserción de datos
# insert_query = "INSERT INTO mi_tabla (columna1, columna2) VALUES (%s, %s)"
# datos_a_insertar = ("valor1", "valor2")
# cursor.execute(insert_query, datos_a_insertar)
# cnx.commit()  # Confirmar la inserción

cursor.close()  # Cerrar el cursor y la conexión
cnx.close()


# 27 Flask:
# Ejemplo 1
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hola, mundo!"


@app.route("/items")
def items():
    items_list = ["item1", "item2", "item3"]
    return render_template("items.html", items=items_list)


# Ejemplo 2
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Bienvenido a mi aplicación web"


@app.route("/saludar")
def saludar():
    nombre = request.args.get("nombre")
    return f"Hola, {nombre}!"


@app.route("/formulario")
def formulario():
    return render_template("formulario.html")


@app.route("/procesar_formulario", methods=["POST"])
def procesar_formulario():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    return f"Gracias por enviar el formulario, {nombre} {apellido}!"


if __name__ == "__main__":
    app.run()


# 28 FastApi
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# 29 matplotlib
import matplotlib.pyplot as plt

# Datos para el gráfico
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Crear el gráfico
plt.plot(x, y)

# Añadir etiquetas al eje x y y
plt.xlabel("Eje x")
plt.ylabel("Eje y")

# Mostrar el gráfico
plt.show()


# 29
from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()


# Buttons
def action():
    print("Do something")


# calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(
    text="Is On?", variable=checked_state, command=checkbutton_used
)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(
    text="Option1", value=1, variable=radio_state, command=radio_used
)
radiobutton2 = Radiobutton(
    text="Option2", value=2, variable=radio_state, command=radio_used
)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()


# 30
import pandas as pd

# Crear un DataFrame
data = {"Nombre": ["Alice", "Bob", "Charlie"], "Edad": [25, 30, 35]}
df = pd.DataFrame(data)

# Explorar datos
print("Primeras filas del DataFrame:")
print(df.head())

print("\nInformación sobre el DataFrame:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())

# Seleccionar y filtrar datos
print("\nColumna 'Nombre':")
print(df["Nombre"])

print("\nFiltrar filas donde 'Edad' > 30:")
print(df[df["Edad"] > 30])

# Agregar y eliminar columnas
df["Altura"] = [160, 175, 180]  # Agregar una nueva columna
print("\nDataFrame con la columna 'Altura' agregada:")
print(df)

df.drop("Altura", axis=1, inplace=True)  # Eliminar la columna 'Altura'
print("\nDataFrame con la columna 'Altura' eliminada:")
print(df)

# Manipulación de datos
print("\nDataFrame ordenado por 'Edad':")
print(df.sort_values(by="Edad"))

print("\nMedia de 'Edad' por grupo:")
print(df.groupby("Edad").mean())

# Guardar y cargar datos
df.to_csv("datos.csv", index=False)  # Guardar en un archivo CSV
print("\nDataFrame guardado en 'datos.csv'")

nuevo_df = pd.read_csv("datos.csv")  # Cargar datos desde un archivo CSV
print("\nDataFrame cargado desde 'datos.csv':")
print(nuevo_df)
