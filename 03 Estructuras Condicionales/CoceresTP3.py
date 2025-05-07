# Actividades
# 1)
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print ("Sos mayor de edad") # a este condicional se le podrian agregar un control de errores como por ejemplo: que la edad tiene que ser mayor que 0.

# 2)
nota = int(input("Ingre su nota: "))
if nota > 6: #Condicion para determinar si esta aprobado o no
    print("Aprobado")
else: print("Desaprobado")

# 3)
numeroPar = int(input("Ingrese un numero par: "))
if numeroPar % 2 == 0: # Con % podemos obtener el resto de una division. En este caso al dividir por 2 si el resto es 0 es par.
    print("Ha ingresado un número par")
else: print("Por favor, ingrese un número par")

# 4)
catEdad = int(input("Ingrese su edad: "))
if catEdad < 12:
    print("Usted es un niño/a")
elif catEdad >= 12 and catEdad < 18:
    print("Usted es un adolencente")
elif catEdad >= 18 and catEdad < 30:
    print("Usted es adulto/a joven")
elif catEdad >= 30:
    print("Usted es un adulto")
else:
    print("Debe ingresar un numero mayor que 0") #El ejercicio no pedia esta condicion. Pero la agregue para que tenga sentido ya que no puede haber edad negativa.

# 5)
clave = input("Ingrese una contraseña de 8 a 14 caracteres: ")
clave = len(clave) >= 8 and len(clave) <= 14 #Con esta linea redefino la variable clave para obtener el valor unico que necesito en booleano.
if clave: #No necesito compara el valor porque la variable "clave" es un booleano que dependiendo lo que se ingrese va a dar true o false.
    print("Ha ingresado una contraseña correcta")
else: print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6)
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
numeroMean = mean(numeros_aleatorios)
numeroMedian = median(numeros_aleatorios)
numeroMode = mode(numeros_aleatorios)
if numeroMean > numeroMedian and numeroMedian > numeroMode:
    print("Hay sesgo positivo")
elif numeroMean < numeroMedian and numeroMedian < numeroMode:
    print("Hay sesgo negativo")
elif numeroMean == numeroMedian == numeroMode:
    print("No hay sesgo")
else: print("No se puede determinar el sesgo")

# 7)
frase = input("Ingrese una frase: ")
terminaVocal = frase[-1] in ("a", "e", "i", "o", "u") #Tambien se puedo poner frase[len(frase)-1] esto hace referencia al ultimo caracter tambien.
if terminaVocal: #La palabra reservada "in" de la linea anterior te ayuda a verificar si el elemento que elegi contiene lo que le especifico en el parentesis siguiente, o lista, conjunto etc.
    print(frase+"!")
else:
    print(frase)

# 8)
name = input("Ingrese su nombre: ")
print("Seleccione 1 para imprimir su nombre en mayuscula")
print("Seleccione 2 para imprimir su nombre en minuscula")
seleccion = input("Seleccione 3 para imprimir su nombre con la primer letra mayuscula ")
if seleccion == "1":
    print(name.upper())
elif seleccion == "2":
    print(name.lower())
elif seleccion == "3":
    print(name.title())
else: print("Seleccione una opcion valida.")

# 9)
magnitud = int(input("Ingrese la maginitud en la escala de Richter"))
if magnitud > 0 and magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible). ")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños). ")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles). ")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos). ")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala). ")
else:
    print("Debe ingresar un numero mayor que 0")

# 10)
hemisferio = int(input('¿En que hemisferio te encuentras? Ingrese "1" para Norte o "2" para Sur :'))
mes = int(input("¿Que mes del año? ingrese el mes con su respectivo numero"))
dia = int(input("Ingrese el numero del dia del mes"))
if mes in (1 , 2) or (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20):
    if hemisferio == 1:
        print("Estas en invierno")
    elif hemisferio == 2:
        print("Estas en verano")
    else: print("Ingrese un hemisferio valido (1 o 2)")
if mes in (4 , 5) or (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20):
    if hemisferio == 1:
        print("Estas en primavera")
    elif hemisferio == 2:
        print("Estas en otoño")
    else: print("Ingrese un hemisferio valido (1 o 2)")
if mes in (7 , 8) or (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
    if hemisferio == 1:
        print("Estas en verano")
    elif hemisferio == 2:
        print("Estas en invierno")
    else: print("Ingrese un hemisferio valido (1 o 2)")
if mes in (10 , 11) or (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20):
    if hemisferio == 1:
        print("Estas en otoño")
    elif hemisferio == 2:
        print("Estas en primavera")
    else: print("Ingrese un hemisferio valido (1 o 2)")