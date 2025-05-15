"""Trabajo practico N°5."""  
import math
#Definicion de funciones
#1
def imprimir_hola_mundo():
    print("Hola mundo!")
#2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
#3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
#4
def  calcular_area_circulo(radio):
    print( math.pi * (radio * radio), "Es el area del circulo")
def calcular_perimetro_circulo(radio):
    print( (2 * math.pi * radio), "Es el perimetro del circulo")
#5
def segundos_a_horas(segundos):
    cant_hora = (segundos / 60) / 60
    print(f" La cantidad de {segundos} segundos, equivale a {cant_hora}hs.")
#6
def tabla_multiplicar(numero):
    for i in range (1, 11):
        print(f"{i} * {numero} = ", i*numero)
#7
def operaciones_basicas(a, b):
    print (f"El resultado de la suma entre {a} y {b} es: ", a+b)
    print (f"El resultado de la resta entre {a} y {b} es: ", a-b)
    print (f"El resultado de la multiplicacion entre {a} y {b} es: ", a*b)
    print (f"El resultado de la division entre {a} y {b} es: ", a/b)
#8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Tu IMC es: {imc:.2f}")
#9
def celsius_a_fahrenheit(celsius):
    f = (celsius * 9/5) + 32
    print(f"La conversion de {celsius}C° a °F es : {f}°F")
#10
def calcular_promedio(a, b, c):
    print(f"El promedio de {a}, {b} y {c} es: ", (a+b+c)/3)

#Programa principal
#1
imprimir_hola_mundo()
#2
saludar_usuario("Hernan")
#3
n = input("Ingrese su nombre: ") #Puse las inicales de el dato a ingresar para hacer mas rapida la sintaxis. Entiendo que debe ser descriptiva la variable
a = input("Ingrese su apellido: ")
e = input("Ingrese su edad: ")
r = input("Ingrese su residencia: ")
informacion_personal(n, a, e, r)
#4
radio = int(input("Ingrese el radio del circulo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)
#5
segundos = int(input("Ingrese una cantidad de segundos a convertir en hora/s: "))
segundos_a_horas(segundos)
#6
tabla = int(input("Ingrese un numero para saber su tabla del 1 al 10: "))
tabla_multiplicar(tabla)
#7
a = int(input("Ingrese el primer numero para calcular: "))
b = int(input("Ingrese el segundo numero para calcular: "))
operaciones_basicas(a,b)
#8
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))
calcular_imc(peso,altura)
#9
celsius = float(input("Introduce una temperatura en C° para saber cuanto es en °F: "))
celsius_a_fahrenheit(celsius)
#10
num1 = float(input("Introduce el primer numero para calcular el promedio: "))
num2 = float(input("Introduce el segundo numero para calcular el promedio: "))
num3 = float(input("Introduce el tercer numero para calcular el promedio: "))
calcular_promedio(num1,num2,num3)