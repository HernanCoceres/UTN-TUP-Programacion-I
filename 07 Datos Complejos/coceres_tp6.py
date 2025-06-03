"""
TRABAJO PRACTICO 6 . DATOS COMPLEJOS
"""
#1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200 #De esta forma puedo agregar una clave y valor
precios_frutas['Manzana'] = 1500 #Si existe lo reemplaza y si no lo agrega
precios_frutas['Pera'] = 2300

#2
precios_frutas['Banana'] = 1330 #De la misma forma puedo actualizar los precios
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas) #imprimo por pantalla para corroborar.

#3
frutas_sinPrecio = [precios_frutas.keys()] #Creo una lista nueva, con las keys del diccionario
print(frutas_sinPrecio) #Para obtener solo las frutas

#4
agenda = {} #Declaro el diccionario vacio
def agregar_contacto(name,num): #Creo una funcion que me permite agregar clave y valor al diccionario
    agenda[name] = num
for i in range(0,5): #Creo un bucle que me pida los datos 5 veces como lo pide la consigna
    name = input("ingrese el nombre del contacto: ") #Guardo el dato en name
    num = input('ingrese el numero de contacto: ') #Guardo el dato en num
    agregar_contacto(name,num) #Le paso como argumento las variables que necesita la funcion para agregar a agenda el contacto
name_solicitado = input("ingrese el nombre del contacto para brindarle su numero: ") #Pido al usuario un nombre de contacto
if name_solicitado in agenda: #Y con un condicional valido si esta el nombre en la agenda
    print(f"El numero de {name_solicitado} es : {agenda[name_solicitado]}") # Si esta le digo su numero
else:
    print("EL nombre ingresado no pertenece a la lista de contactos") #Si no esta le digo que no existe

#5
frase = input("Ingrese una frase: ") #primero solicito al usuario que ingrese una frase
palabras = set(frase.split()) #paso la frase a un set en donde elimina las palabras repetidas y solo devuelve las palabras usadas
print(f"Tu frase contiene estas palabras únicas: {palabras}") #muestro las palabras

cantidad_palabras = {} # defino un diccionario
palabras_repetidas = frase.split() # creo una lista con todas las palabras de la frase

def agrega_palabras(pal, can): #creo una funcion para agregar llaves y valores a el diccionario
    cantidad_palabras[pal] = can

for pal in palabras_repetidas: #Entonces defino un bucle para iterar con todas las palabras de la lista
    if pal in cantidad_palabras: #Si pal esta en cantidad de palabras
        cantidad_palabras[pal] += 1 #Enotnces agrego 1 a el valor de la key de la palabra iterada
    else: #Si no esta en el diccionario
        agrega_palabras(pal, 1) #entonces uso la funcion para agregar la llave y el valor al diccionario
print(cantidad_palabras) #Muestro en pantalla las palabras con sus respectivos valores, que se entienden por repetidas o cantidad

#6
notas_alumnos = {} #Defino un diccionario para almacenar los 3 alumnos que ingresa el usuario
def crear_alumnos (nombre,n1,n2,n3): #creo una funcion que me va a permitir crear un alumno dentro de un diccionario.
    notas_alumnos[nombre] = (n1,n2,n3) #armo la estructura que va a tener el diccionario
for i in range (0,3): #Creo el bucle para que el usuario ingrese 3 alumnos con 3 notas
    nombre = input("ingrese el nombre del alumno: ")
    n1 = int(input("Ingrese una nota del alumno: "))
    n2 = int(input("Ingrese una nota del alumno: "))
    n3 = int(input("Ingrese una nota del alumno: "))
    crear_alumnos(nombre,n1,n2,n3) #Uso los input para darle argumentos a la funcion que crea los alumnos

for nombre, notas in notas_alumnos.items(): #Hago un bucle calcular los promedios de los elementos del diccionario
    promedio = sum(notas) / len(notas) #uso la funcion integrada de python para poder sumar todas las notas y las promedio
    print(f"{nombre} tiene un promedio de: {promedio:.2f}") #Muestro los resultados y uso .2f para mostrar solo 2 ddecimales

#7
parcial_1 = {1, 2, 3, 4, 5} #Defino los dos sets que representan los alumnos con su nota
parcial_2 = {3, 4, 6, 7, 8}
aprobados_ambos = parcial_1 & parcial_2 #Defino los alumnos que aprobaron ambos parciales con el operador and
print(f"Aprobaron ambos parciales: {aprobados_ambos}") #Y muestto por pantalla

aprobados_solo_uno = parcial_1 ^ parcial_2 #Defino los alumnos que aprobaron solo 1 de los 2 con el operador de XOR
print(f"Aprobaron solo uno de los dos: {aprobados_solo_uno}")#Muestro por pantalla

aprobados_total = parcial_1 | parcial_2 #Defino que alumnos aprobaron con el operador | que cuando lo usamos en sets devuelve la union
print(f"Lista total de aprobados: {aprobados_total}")
#PD: No era muy especifico el problema pero entendi que la intencion era que usemos iterseccion, union y diferencia. Espero que este bien asi. Porque no podia identidicar un alumno con un set asignando un valor a cada key, porque un set no es un diccionario.

#8 Defino la lista de productos inicial
stock_productos = {
    "Harina": 50,
    "Leche": 30,
    "Arroz": 20
}
def consulta_stock(): #Defino la funcion para consultar stock
    producto = input("Ingrese el nombre del producto: ") #Solicito el producto
    if producto in stock_productos:  # Si existe en la lista
        print(f"El producto {producto} tiene {stock_productos[producto]} unidades de stock") #Enotnces muesto el stock
    else:
        print("El producto ingresado no se encuentra en la lista de productos")# Sino  existe entonces muestro el mensaje

def agregar_unidades():
    producto = input("Ingrese el nombre del producto: ")
    unidades = int(input("Ingrese las unidades que agrega del producto: "))
    if producto in stock_productos: #Si el producto ingresado existe en la lista
        stock_productos[producto] += unidades #Entonces agrego las unidades
        print(f"Se agregaro {unidades} unidades al producto {producto}")
    else: #Si no esta entonces muestro el siguiente mensaje
        print(f"El producto {producto} no existe en el stock actual, por favor ingrese la opcion 3 para agregarlo.")

def agregar_producto():
    producto = input("Igrese el nombre del producto: ")
    if producto in stock_productos: #Si el producto existe
        print("El producto que ingreso ya existe en la lista.") #Aviso que ya esta
    else:
        unidades = int(input("Ingrese la cantidad de unidades para agregar: ")) #Si no esta pido las unidades
        stock_productos[producto] = unidades #agrego el producto con su respectiva unidades

def decision():
    return int(input("Ingrese qué desea hacer:\n"
                     "Si terminar el programa ingrese 0\n"
                     "Si desea consultar el stock ingrese 1\n"
                     "Si desea agregar unidades al stock de un producto ingrese 2\n"
                     "Si desea agregar un producto ingrese 3\n"))

res = decision()  #Guardo el valor de la funcion en res

while res != 0:
    if res == 1:
        consulta_stock()
    elif res == 2:
        agregar_unidades()
    elif res == 3:
        agregar_producto()
    else:
        print("Debe ingresar un valor válido")
    res = decision()  # Pido una nueva decision en caso de que se equivoque el usuario

#9
agenda = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Martes", "15:00"): "Clase de programación",
    ("Miércoles", "18:00"): "Gimnasio"}

#10
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {capital: pais for pais, capital in original.items()}
print(invertido)
