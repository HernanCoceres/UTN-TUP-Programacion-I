"""Tp 6 Recursividad"""
#1
def fact_recur(n): #Primero realizo la funcion recursiva para obtner el factorial
    if n == 1:
        return 1
    else:
        return n * fact_recur(n-1)
    
def fact_todos(n): #Con esta funcion voy a imprimir todos los factoriales de los numeros
    for i in range (1,n+1): #Uso un for porque ya se cuantas iteraciones voy a tener son de 1 a el numero que ingrese el usuario (le sumo 1 a "n" para que incluya el numero ingresado)
        print(f"El factorial de {i} es: {fact_recur(i)}") #Imprimo todos los valores de factoriales del 1 al numero que ingreso el usuario
fact_todos(4)

#2
def recur_fibo(posicion): #Defino la funcion recursiva para calcular la serie de fibo
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return recur_fibo(posicion-1)+recur_fibo(posicion-2)
def mostrar_serie(n): #Creo la funcion para mostrar todos los valores de fibo hasta el numero que ingresa el usuario
    print("Esta es la serie de fibo hasta el numero que ingreso:") #Aclaro lo que va a imprimir el programa
    for i in range (0,n+1): #Uso el bucle para mostrar todos los valores de fibo desde el 0 hasta el numero ingresado por el usuario
        print(recur_fibo(i)) #imprimo todos los valores de i que serian los resultados de la serie de fibo
mostrar_serie(7)

#3
a = int(input("Ingrese un valor para calcular su potencia: ")) #Creo el algoritmo para que calcular la potencia
b = int(input("Ingrese el valor de la potencia: ")) #Solicitando valores para saber que calcular
def potencia(a,b): #Creo la funcion recursiva para calcular la potencia
    if b == 0:
        return 1
    else:
        return a * potencia(a,b-1)
print(f"El valor de la potencia es: {potencia(a,b)}")

#4
c = int(input("Ingrese un numero decimal para obtener su valor en binario: "))
def decimal_a_binario(n): #Creo la funcion recursiva para converti el numero decimal a binario
    if n == 0: #Si n es 0 no es necesario calcular nada 0 en decimal es 0 en binario
        return "0"
    elif n == 1: #Lo mismo 1 decimal == 1 binario 
        return "1"
    else: #Se hace recursiva la funcion dividiendose por 2 hasta que llege al caso base y concateno los residuos para tener el numero en binario
        return decimal_a_binario(n // 2) + str(n % 2) #utilizo el str para convertir el valor a cadena asi el "+" puede concatenar y no hacer la operacion de suma que no me serviria en este caso
print(f"El valor en binario del numero decimal ingresado es: {decimal_a_binario(c)}") #imprimo el resultado

#5
palabra = input("Ingrese una palabra para saber si es un palindromo: ")
def palindromo(palabra):
    if len(palabra) <= 1: #El caso base es como una validacion en este caso si se ingresa 1 letra tecnicamente es un palindromo tambien
        return True #Entonces devuelvo true
    if palabra[0] != palabra[-1]: #Con esta condicion comparo la primer letra con la ultima, palabra[-1] me devuelve la ultima letra
        return False #Si son distintas quiere decir que no es un palindromo, porque deben ser iguales comparando los extremos de la posicion por asi decirlo.
    return palindromo(palabra[1:-1]) #Hago la llamada recursiva de la cadena pero esta vez elimino el primer y ultimo caracter porque ya los verifique anteriormente de que son iguales
#Entonces la palabra se achica hasta que sea igual o menor a 1 y quiere decir que es una palindromo en ese caso, entonces devuelve true. Pongo menor o igual porque si la palabra es..
#par enotnces la palabra puede valer 0 y si es impar la palabra puede valer 1. Osea no vale 1 pero me refiero a su longitud que obtengo con "len()"
print(palindromo(palabra))

#6
z = int(input("ingrese un numero entero positivo para sumar sus digitos: "))
def suma_digitos(z):
    if z == 0: #Cuendo llege a cero quiere decir que no hay mas numeros, por eso pongo el caso base en 0
        return 0
    else: #Uso z%10 para tener el ultimo digito, como el numero es decimal osea base 10 entonces siempre el resto de dividir por 10 me va a dar el ultimo numero
        return (z % 10) + suma_digitos(z // 10) #Y lo mismo en este caso de "z//10" como es base 10 al el cociente de divir por 10 me va devolver el mismo numero sin el ultimo
#Enotnces sumo el ultimo numero con el siguiente ultimo numero, como no lo sabe tiene que hacer la llamada recursiva hasta llegar a 0
print(f"La suma de todos los digitos del numero {z} es : ",suma_digitos(z))

#7
x = int(input("Ingrese la base de bloques para saber la cantidad que necesita para formar una piramide: "))
def contar_bloques(x):
    if x <= 0: #En el caso de que ingrese un numero negativo, o 0 entonces no es necesario hacer la llamada recursiva porque ya sabemos que no hay piramide con bloques negativos o cero
        return 0
    elif x == 1: #En el caso que ponga 1 no se puede formar piramide con mas bloques entonces queda 1 solo bloque
        return 1
    else: #En los casos de que sea mas de 1 entonces calculo y sumo todos los valores de x-1 que serian todas las siguientes filas de bloques hasta llegar a que retorne 1, entonces suma todo
        return x + contar_bloques(x-1) #X es la base que ingreso y x-1 representa todas las cantidades de bloques por fila hasta llegar a la punta
print(f"La cantidad necesaria para formar una piramide con base {x} es: {contar_bloques(x)}")

#8
numero = int(input("Ingrese un numero: "))
digito = int(input("Ingrese que numero desea saber cuantas veces se repite en el numero ingresado anterior: "))
def  contar_digito(numero, digito):
    if numero == 0: #Pongo el caso base en 0 porque quiere decir que ya no hay numeros para comparar
        return 0
    elif (numero%10) == digito: #Esta condicion quiere decir que si el ultimo numero es igual al digito entonces se repite
     return 1 + contar_digito(numero//10, digito) #Por ende si se repite debo sumar 1
    else:
        return contar_digito(numero//10,digito) #Si no se repite y numero no es cero entonces vuelvo a ejecutar con el siguiente numero
print(f"La cantidad de veces que se repite el numero {digito} en {numero} es: ", contar_digito(numero,digito))#Al final me devuelve la suma de todos los 1, que quiere decir la cantidad de veces que se repite.