# TRABAJO PRÁCTICO Nº 4 ESTRUCTURAS CONDICIONALES.

# 1. Determinar si un número leído es positivo.

# numero= int(input("Ingrese un numero: "))
# if numero > 0: print("el numero leido es positivo")

# 2. Mostrar si un número es mayor que 10.

# numero= int(input("Ingrese un numero: "))
# if numero > 10: print("el numero leido es mayor que 10")

# 3. Leer el nombre y sueldo de una persona mostrar si este gana más de 30.000 pesos.

# nombre= input("Ingrese el  nombre de la persona: ")
# sueldo= int(input("Ingrese sueldo de la persona: "))
# if sueldo > 30000: print(nombre,"gana mas de $30000")

# 4. Dados dos números si el primero es divisible por el segundo mostrar un mensaje que así lo indique.

# numero_a= int(input("Ingrese un numero: "))
# numero_b= int(input("Ingrese un numero: "))
# if ( (numero_a%numero_b) == 0) : print(numero_a,"es divisible por",numero_b)


# 5. Ingresar un par de valores, emitirlos, y si ambos son positivos, emitir también su promedio.

# valor_1= int(input("Ingrese valor 1: "))
# valor_2= int(input("Ingrese valor 2: "))

# print("valor 1:",valor_1)
# print("valor 2:",valor_2)
# if ( valor_1 >0 and valor_2 >0): print("promedio:",(valor_1+valor_2)//2)

# 6. Dados dos números si el primero es divisible por el segundo intercambiarlos.

# numero_a= int(input("Ingrese un numero: "))
# numero_b= int(input("Ingrese un numero: "))

# if ( (numero_a%numero_b) == 0) :
#   auxiliar = numero_a
#   numero_a = numero_b
#   numero_b = auxiliar
#   print("numero a: ",numero_a)
#   print("numero b: ",numero_b)

# 7. Deducir si un número leído (distinto de cero) es positivo o negativo.

# numero= int(input("Ingrese un numero: "))

# if numero != 0:
#   if numero >0:
#     print("el numero leido es positivo")
#   else:
#     print("el numero leido es negativo")

# 8. Dados tres números enteros positivos, determinar cuál es el mayor.

# numero_1= int(input("Ingrese el  numero 1: "))
# numero_2= int(input("Ingrese el  numero 2: "))
# numero_3= int(input("Ingrese el  numero 3: "))

# if (numero_1  >= 0 and  numero_2 >= 0 and numero_3 >= 0):
#   if numero_1 >numero_2 and numero_1 >numero_3:
#     print("el numero 1 es el mayor ")
#   elif numero_2 >numero_3 and numero_2 >numero_1:
#     print("el numero 2 es el mayor")
#   else:
#     print("el numero 3 es el mayor ")

# 9. Escribir un programa que muestre un mensaje afirmativo si el número introducido es múltiplo de 5.

# numero= int(input("Ingrese un  numero: "))
# if (numero%5)==0: print("el numero ",numero," es multiplo de 5")

# 10. Leer tres letras, encontrar y visualizar cuál viene primero en el alfabeto.

# letra_1 = input("Ingrese letra 1 : ").lower()
# letra_2 = input("Ingrese letra 2 : ").lower()
# letra_3 = input("Ingrese letra 3 : ").lower()


# if letra_1 < letra_2 and letra_1 < letra_3:
#     print("la letra ",letra_1," viene primero en el alfabeto")
# elif letra_2 < letra_3 and letra_2 < letra_1:
#     print("la letra ",letra_2," viene primero en el alfabeto")
# else:
#     print("la letra ",letra_3," viene primero en el alfabeto")

# 11. Confeccionar un algoritmo tal que dados dos números enteros:
# devuelva la suma de los mismos si se cumple que el primero es menor que el segundo
# en caso contrario devolver el producto de los mismos.

# numero1= int(input("Ingrese el numero 1: "))
# numero2= int(input("Ingrese el numero 2: "))

# if numero1<numero2:print(numero1+numero2)
# else:print(numero1*numero2)

# 12. Se ingresa el nombre, edad y dirección de dos socios, se pide mostrar los datos de socio más joven.

# nombre1 = input("Ingrese el nombre del socio 1 ")
# edad1 = int(input("Ingrese la edad del socio 1 "))
# direccion1 = input("Ingrese la direccion del socio 1 ")
# nombre2 = input("Ingrese el nombre del socio 2 ")
# edad2 = int(input("Ingrese la edad del socio 2 "))
# direccion2 = input("Ingrese la direccion del socio 2 ")

# if edad1<edad2: print(nombre1,edad1," años. Direcion:",direccion1)
# else: print(nombre2,edad2," años. Direcion:",direccion2)


# 13.	Escriba un programa que permita el ingreso de un número de tres dígitos y determine:
# si es un número Armstrong (ej. 153, 371). 
# Como el número que se ingresa posee 3 dígitos, la suma de cada uno de sus dígitos elevado a 3 debe ser igual al número.

# digitos = input("Ingrese un numero de 3 digitos: ")

# if len(digitos) != 3: print("Usted ingreso un numero diferente a 3 digitos")

# digito1  = int(digitos[0])
# digito2  = int(digitos[1])
# digito3  = int(digitos[2])
# posibleAmstrong = int(digitos)


# if digito1**3 + digito2**3 + digito3**3 ==  posibleAmstrong : print(posibleAmstrong," Es un numero amstrong")
# else: print(posibleAmstrong," no es amsotrong")


# 14.	Desarrollar un algoritmo que una vez leída una Fecha en formato dd/mm/aaaa, indique cual será la fecha un día después.

# Aclaracion: LA RESOLUCION DE ESTE PROBLEMA NO TIENE EN CUENTA LOS AÑOS BISIESTOS!!!

# dia= int(input("Ingrese el dia: "))
# mes= int(input("Ingrese el mes: "))
# año= int(input("Ingrese el año: "))

# if dia < 0 or dia > 31 or mes <0 or mes >12: print("Usted ingreso una fecha incorrecta para el calendario juliano")
# elif dia >29 and mes == 2:  print("Usted ingreso una fecha incorrecta")
# elif dia >30 and mes == 4 or mes == 6 or mes == 9 or mes == 11:  print("Usted ingreso una fecha incorrecta")
# elif mes == 12 and dia == 31: print(f"mañana sera: 01/01/{año+1}")
# elif mes == 2 and dia == 29: print(f"mañana sera: 01/0{mes+1}/{año}")
# elif mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia == 30: print(f"mañana sera: 01/0{mes+1}/{año}")
# elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or  mes == 8 or mes == 10 or mes == 12 and dia == 31: print(f"mañana sera: 01/0{mes+1}/{año}")
# else: print(f"mañana sera: {dia+1}/0{mes}/{año}")



# 15.	Dados tres nombres de alumnos, mostrar si Mariana Ríos se encuentra entre ellos, de lo contrario emitir un mensaje “No existe”.

# nombre1 = input("ingrese 1° nombre: ")
# nombre2 = input("ingrese 2° nombre: ")
# nombre3 = input("ingrese 3° nombre: ")

# if nombre1== "Mariana Rios" or nombre2== "Mariana Rios" or nombre3== "Mariana Rios":
#   print("Mariana Rios Se encuentra entre los nombres mencionados")
# else: print("No exise")


# 16. Calcular el descuento considerando que para un monto mayor de $ 1000.
# - el descuento es del 10%
# - caso contrario es del 2%. 
#  Se pide mostrar monto con descuento incluido.

# monto = float(input("Ingrese el monto que gasto: $"))
# if monto>1000: print("usted obtuvo un descuento del 10%, Monto final: $",monto-monto*0.1)
# else: print("usted obtuvo un descuento del 2%, Monto final: $",monto-monto*0.02)

# 17.	Escribir un algoritmo en el que se introduzca el número de un mes (1 a 12)
# y visualice el Nº de días de ese mes. (no considerar año bisiesto)

# mes = int(input("Ingrese un numero del mes: "))

# if mes >12 or mes <1: print("El numero ingresado debe estar entre 1 y 12")
# elif mes ==1: print("enero Tiene 31 dias")
# elif mes ==2: print("Febrero Tiene 28 o 29 dias")
# elif mes ==3: print("Marzo Tiene 31 dias")
# elif mes ==4: print("Abril Tiene 30 dias")
# elif mes ==5: print("Mayo Tiene 31 dias")
# elif mes ==6: print("Junio Tiene 30 dias")
# elif mes ==7: print("Julio Tiene 31 dias")
# elif mes ==8: print("Agosto Tiene 31 dias")
# elif mes ==9: print("Septiembre Tiene 30 dias")
# elif mes ==10: print("Octubre Tiene 31 dias")
# elif mes ==11: print("Noviembre Tiene 30 dias")
# elif mes ==12: print("Diciembre Tiene 31 dias")


# 18.	 Emular una calculadora en la cual se ingresan 2 números y el operador (*, /, +, -) e imprime el resultado.

# numero1 = int(input("Ingrese el numero 1: "))
# numero2 = int(input("Ingrese el numero 2: "))
# operador = input("Ingrese el operador (*, /, +, -) ")

# if operador == "+": print(numero1+numero2)
# elif operador == "-": print(numero1-numero2)
# elif operador == "*": print(numero1*numero2)
# elif operador == "/": print(numero1/numero2)
# else: print("usted no ingreso un operador valido")

# 19.	Leer dos números. Decir si el primero es divisible por el segundo, si esto se cumple decir si es un número par o impar.

# numero1 = int(input("Ingrese el numero 1: "))
# numero2 = int(input("Ingrese el numero 2: "))

# if numero1 % numero2 == 0:
#     print("El primer numero ingresado es divisible por el segundo.")
#     if numero1 % 2 == 0:
#         print("Además, el primer numero es par.")
#     else:
#         print("Además, el primer numero es impar.")
# else:
#     print("El primer numero ingresado no es divisible por el segundo.")

# 20.	Leer un número, si dicho número está comprendido entre 23 y 54, decir si es múltiplo de 3 o de 5.

# numero = int(input("Ingrese un numero: "))

# if numero <= 54 and numero >=23:
#   if numero%3==0: print("el numero indicado es multiplo de 3")
#   if numero%5==0: print("el numero indicado es multiplo de 5")

# 21.	Dadas las 4 notas obtenidas por un alumno, calcular su promedio y mostrarlo 
# indicar si está aprobado o no, Se aprueba con un promedio es mayor o igual que 4. 

# nota1 = int(input("Ingrese la 1° Nota: "))
# nota2 = int(input("Ingrese la 2° Nota: "))
# nota3 = int(input("Ingrese la 3° Nota: "))
# nota4 = int(input("Ingrese la 4° Nota: "))

# promedio = (nota1+nota2+nota3+nota4)/4

# print("su promedio es",promedio)
# if promedio>=4:
#   print("esta aprobado ")
# else: print("esta desaprobado")



# 21. La tarifa de un TAXI en Europa es la siguiente:
# - Una cantidad fija de 20 euros, sino se sobrepasan los 30 km.
# - Para más de 30 km, se considerarán los siguientes supuestos:
# ▪ Si no se sobrepasan los 100 km, 1 euro por km, que exceda de los 30, además de los 20 euros.
# ▪ Si sobrepasa los 100 km: 
#  0,50 céntimos por km que exceda de los 100.
#  1 euro por km desde los 30 a los 100 y los 20 euros. 
# Diseñar un programa que pida los kilómetros recorridos y calcule el total a pagar según la tarifa anterior.


# kilmetros = int(input("Ingrese los kilometros recorridos: "))

# if kilmetros<30:
#   print("usted debe pagar un total de 20€ ")
# elif kilmetros > 100:
#   print("usted debe pagar un total de: ",90+(0.50*(kilmetros-100)),"€")
# else:
#   print("ueste debe pagar un total de : ",20+kilmetros-30,"€")


# 23.	Dados 3 números, informarlos en orden creciente.


# numero1 = int(input("Ingrese el 1° numero: "))
# numero2 = int(input("Ingrese el 2° numero: "))
# numero3 = int(input("Ingrese el 3° numero: "))

# if numero1 < numero2 and numero1 < numero3:
#     if numero2 < numero3:
#         print(numero1, numero2, numero3)
#     else:
#         print(numero1, numero3, numero2)
# elif numero2 < numero1 and numero2 < numero3:
#     if numero1 < numero3:
#         print(numero2, numero1, numero3)
#     else:
#         print(numero2, numero3, numero1)
# else:
#     print(numero3, numero1, numero2)



# 24. De una prueba de nivel realizada a un alumno se conoce:
# la cantidad total de preguntas realizadas y la cantidad de respuestas correctas.
# Informar el nivel registrado de acuerdo a la siguiente escala:
# ▪ Muy Bueno si el porcentaje es mayor o igual a 90%
# ▪ Bueno entre 70% y 90%
# ▪ Regular entre 50% y 70%
# ▪ Malo si el porcentaje es menor que 50%

# preguntas = int(input("Ingrese la cantidad total de preguntas realizadas: "))
# respuestas = int(input("Ingrese la cantidad total de respuestas correctas: "))

# nivel = (respuestas*100)/preguntas

# if nivel >=90:print("Muy bueno")
# elif nivel >70 and nivel <90:print("Bueno")
# elif nivel >50 and nivel <70:print("Regular")
# else: print("Malo")



# 25.	Se realiza una encuesta de aceptación de tres productos (se ingresa el porcentaje de cada uno) 
# se busca determinar cuál de ellos es el menos aceptado y el más aceptado.
# Imprimir un mensaje indicando el nombre de los productos y sus porcentajes.

# producto1 = input("Ingrese el nombre del 1° producto: ")
# encuesta1 = float(input(f"Ingrese el porcentaje de aceptación de {producto1}: "))
# producto2 = input("Ingrese el nombre del 2° producto: ")
# encuesta2 = float(input(f"Ingrese el porcentaje de aceptación de {producto2}: "))
# producto3 = input("Ingrese el nombre del 3° producto: ")
# encuesta3 = float(input(f"Ingrese el porcentaje de aceptación de {producto3}: "))

# # Determinar el producto más aceptado
# if encuesta1 > encuesta2 and encuesta1 > encuesta3:
#     producto_mas_aceptado = producto1
#     encuesta_mas_aceptada = encuesta1
# elif encuesta2 > encuesta3:
#     producto_mas_aceptado = producto2
#     encuesta_mas_aceptada = encuesta2
# else:
#     producto_mas_aceptado = producto3
#     encuesta_mas_aceptada = encuesta3

# # Determinar el producto menos aceptado
# if encuesta1 < encuesta2 and encuesta1 < encuesta3:
#     producto_menos_aceptado = producto1
#     encuesta_menos_aceptada = encuesta1
# elif encuesta2 < encuesta3:
#     producto_menos_aceptado = producto2
#     encuesta_menos_aceptada = encuesta2
# else:
#     producto_menos_aceptado = producto3
#     encuesta_menos_aceptada = encuesta3

# # Imprimir los resultados
# print("El producto más aceptado es:", producto_mas_aceptado, "con un porcentaje de aceptación del", encuesta_mas_aceptada, "%.")
# print("El producto menos aceptado es:", producto_menos_aceptado, "con un porcentaje de aceptación del", encuesta_menos_aceptada, "%.")

# 26. Se desea escribir el nombre del día de la semana en función de un número del día.
#  donde 1 es Domingo, 2 es Lunes, y así sucesivamente...

# dia = int(input("Ingrse el numero de un dia de la semana: "))

# if dia < 1 or dia > 7:
#   print("Usted ingreso un numero incorrecto")
# elif dia ==1:print("Domingo")
# elif dia ==2:print("Lunes")
# elif dia ==3:print("Martes")
# elif dia ==4:print("Miercoles")
# elif dia ==5:print("Jueves")
# elif dia ==6:print("Viernes")
# else:print("Sabado")
