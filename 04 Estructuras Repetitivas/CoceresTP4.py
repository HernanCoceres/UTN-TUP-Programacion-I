import math, random
# Actividad 1)
for i in range (1,101):
    print(i)

# 2) En este ejercicio uso la libreria de math para poder usar su funcion que me ayuda a saber cuantos digitos contiene el numero ingresado.
cantDigitos = math.floor(math.log10(int(input("Igrese un numero para saber cuantos digitos contiene: ")))) + 1 # Al final le sumo 1 porque empieza contando desde 0
print(f"Contiene {cantDigitos} digitos")

# 3)
desde = int(input("Elija un numero desde donde empieza el rango: "))+1 #le sumo 1 porque el rango no incluye el numero ingresado
hasta = int(input("Elija un numero hasta donde termina el rango: "))
sumatoria = 0 #inicio el acumulador en 0, para que sume todos los valores del rango
if desde <= hasta: #Agrego la condicion para que el rango sea valido, como sumo uno por eso pongo mayor o igual.Si se ingresa por ejemplo 1 y 2, no existe rango de numero entero por ende el resulta 0.
    for i in range (desde, hasta):
        sumatoria = sumatoria+i
else:
    print("El numero que inicia el rango debe ser menor al que lo termina. Por ende su resultado va a ser 0 como se muestra a continuacion.")
print(sumatoria, "es la suma de todos lo numeros en el rango. Excluyendo los numeros ingresados")

# 4)
sumaSecuencia = int(input("Ingrese un numero para sumar: ")) #pido el primer numero para sumar
sumaSecuencia2 = "0" #inicializo la variable en un string para que pueda entrar en el bucle
while sumaSecuencia2 !=0: #mientras que la variable sea distinta de cero se va a ejecutar
    sumaSecuencia2 = int(input("Ingrese otro numero para sumar o cero para finalizar: ")) #Con esto hago que lo que ingrese reemplace al valor que tenia antes del bucle
    sumaSecuencia = sumaSecuencia+int(sumaSecuencia2) #utilizo la primer variable como un acumulador sumandole todos los valores que ingrese el usuario cada vez que itere el bucle
    print(sumaSecuencia) #muestro el resultado cada vez que itera el bucle
print("Se finalizo la suma") #cuando ingrese el usuario el cero, va a salir del bucle por ende sigue esta linea de codigo.

# 5)
numeroAleatorio = random.randint(1, 9) #con la libreria random puedo generar un numero al azar entre los valores que elijo
numUsuario = int(input("Adivina el numero de 1 a 9, ingrese un numero: ")) #solicito que ingrese un numero
intentos = 1 #inicio el los intentos en 1 porque al menos debe hacerlo una vez
while numUsuario != numeroAleatorio: #mientras el numero ingresado sea distinto al numero aleatorio, el bucle va a preguntar hasta que no se cumpla la condicion
    numUsuario = int(input("Ingrese otro numero: ")) #Si no adivino a la primera pedimos otro numero
    intentos += 1 #sumamos otro intento por cada vez que itera el bucle osea otro intento que hace el usuario
print(f"Adivinaste! el numero era el {numeroAleatorio}, lo hiciste en {intentos} intentos.") #muestro el resultado

# 6)
for i in range (98, 0, -2): #inicio el rango en 98 porque me pide los numeros comprendidos entre 100 y 0 por ende 100 no esta dentro del rango.
    print(i)

# 7)
numLimite = int(input("Ingrese el numero hasta el cual desee sumar todos los numeros apartir de 0: "))
acu = 0 #inicializo el acumulador
for i in range (1, numLimite+1): # i va a tomar todos los valores de 0 a el limite que ingrese el usuario
    acu = acu+i #acumulo todas las sumas de i
print(acu)

# 8)
contadorPar = 0 #incializo los contadores en 0
contadorImpar = 0
contadorNegativo = 0
contadorPositivo = 0
for i in range (0,100): # lo probe con un numero menor pero lo dejo en 100 para que cumpla con la consigna.
    ingreso = int(input("ingrese un numero: "))
    if ingreso%2 == 0:
       contadorPar = contadorPar+1
    else:
       contadorImpar = contadorImpar+1
    if ingreso >= 0:
       contadorPositivo = contadorPositivo+1
    else:
       contadorNegativo = contadorNegativo+1
print(f"Usted ingreso: {contadorPar} numeros pares, {contadorImpar} numeros impares, {contadorPositivo} numeros positivos y {contadorNegativo} numeros negativos")

# 9)
acumula = 0
for i in range (0,100): # lo probe con un numero menor pero lo dejo en 100 para que cumpla con la consigna.
    ingreso = int(input("ingrese un numero: "))
    acumula = acumula+ingreso #sumo todos los valores que ingresa el usuario
print(f"El promedio de los numeros ingresados es: {acumula/100}") #divido en 100 para tener el promedio. Si la prueba es con menos cantidad de numeros deberia cambiar la division O agregar y reemplazar por una variable de cantidad.

# 10)
numero = int(input("Ingrese un número: "))
numero_inver = 0
while numero > 0:
    digito = numero % 10  #con esto tengo el ultimo digito
    numero_inver = numero_inver * 10 + digito  # de esta forma lo agrego al numero invertido
    numero //= 10  # Borro el ultimo digito del numero original
print(f"El número invertido es: {numero_inver}")
