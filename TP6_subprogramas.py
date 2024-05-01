# TRABAJO PRÁCTICO Nº 6 SUBPROGRAMAS.

# 1. Escribir un procedimiento Geometría tal que dado el alto y ancho de un rectángulo calcule el área.


# def area_rectanular(alto, ancho):
#     return alto * ancho

# altura =  int(input("ingrese la altura: "))
# anchura = int(input("ingrese la anchura: "))

# print(f"El area del rectangulo es igual a: {area_rectanular(altura,anchura)}")


# 2. Ídem para el perímetro.


# def perimetro_rectanular(alto, largo):
#     return 2*alto + 2*largo

# alto =  int(input("ingrese el alto: "))
# largo = int(input("ingrese el largo: "))

# print(f"El area del rectangulo es igual a: {perimetro_rectanular(alto,largo)}")


# 3. Escribir un procedimiento que calcule el factorial de un Nº entero usando parámetro valor y variable.

# def factorial(numero):
#     if numero == 0:
#         return 1
#     else:
#         return numero * factorial(numero-1)

# num = int(input("Ingresa un número para calcular su factorial: "))

# print("El factorial de", num, "es", factorial(num))


# 4. Escribir los procedimientos correspondientes a la carga y visualización de un arreglo de x elementos.

# def cargar_arreglo():
#   lista= []
#   salir = "no"
#   while salir !="si":
#     elemento = input("ingrese un elemento: ")
#     lista.append(elemento)
#     salir = input("¿desea salir? si/no ").lower()
#   return lista

# print(f"Los elementos de su lista: {cargar_arreglo()}")


# 5. Escribir un programa que acepte un arreglo (no ordenado), un valor cualquiera
# y obtenga la posición del elemento si lo encontró. (Utilizar procedimientos para cada operación).

# def posicion(lista):
#     elemento = input("Ingrese el elemento que desea buscar: ")
#     if elemento in lista:
#         indice = lista.index(elemento)
#         return f"El elemento '{elemento}' se encuentra en la posición {indice}."
#     else:
#         return f"El elemento '{elemento}' no se encuentra en la lista."

# # Ejemplo de uso:
# mi_lista = ['a', 'b', 'c', 'd', 'e']
# print(posicion(mi_lista))

# 6.	Diseñar una función que calcule potencias de forma xn y un programa que haga uso de la misma, para distintos valores de x y n.

# def potencia(x,n):
#     return x**n

# def calcular_potencia():
#     base =   int(input("ingrese la base: "))
#     indice = int(input(("ingrese el indice: ")))
#     return potencia(base,indice)

# print(calcular_potencia())


# 7.	Escribir una función lógica tal que dadas dos cadenas indique si la primera es más larga que la segunda.

# def calcular_potencia():
#   base = int(input("Ingrese la base: "))
#   exponente = int(input("Ingrese el exponente: "))
#   resultado = 0
#   for item in range(exponente):
#     resultado+= base*base
#   return resultado

# print(calcular_potencia())



# 8.	Escribir un programa que, utilizando procedimientos con parámetros.
# lea desde el teclado las unidades y el precio que quiere comprar.
# y en función de las unidades introducidas le haga un descuento o no.


# def descuento():
#   unidades = int(input("Ingrese la cantidad de unidades:"))
#   precio = int(input("Ingrese el precio: "))

#   total = precio*unidades

#   if unidades > 10:
#     return(f"tiene un descuento del 5% , total $ {total-(total*0.05)}")
#   elif unidades > 20:
#     return(f"tiene un descuento del 10% , total $ {total-(total*0.1)}")
#   else: return(f"No obtuvo descuento, total $ {total}")

# print(descuento())


# 9.	Escribir una función par tal que indique si un número es par o impar.

# def par_impar():
#   numero = int(input("ingrese un numero: "))
#   if numero % 2 == 0:
#     return ("el numero ingresado es par")
#   else:  return ("el numero ingresado es impar")

# print(par_impar())


# 10.	Escribir una función que recuba un parámetro de tipo entero.
# y que devuelva la letra P si el Nº es positivo y N si es negativo o cero.

# def positivo_negativo(numero):
#   if numero > 0:
#     return f"{numero} es positivo"
#   elif numero <0:
#     return f"{numero} es negativo"
#   else: return "el numero ingresado es 0"

# print(positivo_negativo(2))


# 11.	Escribir una función lógica de dos parámetros enteros que devuelva True si uno divide al otro y False en caso contrario.

# def divisores(n1,n2):
#   if n1 % n2 == 0 or n2 % n1 == 0:
#     return True
#   else: return False

# print(divisores(4,8))

# 12.	Escribir un procedimiento digito, que determine si un carácter es uno de los dígitos de o a 9.

# def digito(caracter):
#     return caracter.isdigit() and int(caracter) >= 0 and int(caracter) <= 9

# print(digito('5'))  # True
# print(digito('a'))  # False
# print(digito('12')) # False


# 13.	Escribir una función lógica vocal que determine si un carácter es una vocal.

# def vocal(caracter):
#   eval = caracter.lower()
#   if eval == "a" or eval == "e" or eval == "i" or eval == "o" or eval == "u":
#     return "es vocal"
#   else: return "no es vocal"

# 14.	Escribir un procedimiento que permita calcular la suma 1+2+3+ ... + n.

# def suma_serie(numero):
#     suma = 0
#     for item in range(1, numero+1):
#         suma = suma + item
#     return suma

# 15.	Escribir un procedimiento tipo calculadora
# donde se le da como entrada dos números y el tipo de operación y esta devuelve el resultado.


# def calculadora(n1, n2):
#     operacion = ""

#     print("Ingrese operación a realizar | Escriba X para salir ")
#     print("S: Suma")
#     print("R: Resta")
#     print("M: Multiplicación")
#     print("D: División \n")

#     while operacion != "X":
#         operacion = input().upper()
#         if operacion == "S":
#             resultado = n1 + n2
#         elif operacion == "R":
#             resultado = n1 - n2
#         elif operacion == "M":
#             resultado = n1 * n2
#         elif operacion == "D":
#             if n2 != 0:
#                 resultado = n1 / n2
#             else:
#                 print("La división por cero no es válida.")
#                 continue
#         elif operacion == "X":
#             print("Saliendo de la calculadora...")
#             break
#         else:
#             print("Operación inválida")
#             continue
#         print("El resultado de la operación es:", resultado)

# 16.	Escribir una función que dados 2 números, calcule el porcentaje que el primero representa respecto del segundo.

# def porcentaje():
#   n1 = int(input("Ingrese el Primer valor: "))
#   n2 = int(input("Ingrese el Segundo valor: "))

#   porcentaje = n1*100/n2

#   return f"El porcentaje de {n1} sobre {n2} es %{porcentaje}"


# print(porcentaje())