# TRABAJO PRÁCTICO Nº 5 CICLOS

# 1. Ingresar 5 pares de valores, en cada oportunidad emitir ambos valores y si ambos son positivos, emitir también su promedio.

# for item in range(5):
#   print("par numero: ", item+1)
#   valor1= int(input("ingrese 1° valor: "))
#   valor2= int(input("ingrese 2° valor: "))
#   print("valor 1: ", valor1)
#   print("valor 2: ", valor2)
#   if valor1>0 and valor2>0:
#     print((valor1+valor2)/2)


# 2. Calcular la suma y el producto de los números pares comprendidos entre 20 y 500.

# suma = 0
# producto = 1

# for pares in range(20, 501, 2):  # Itera sobre números pares desde 20 hasta 500
#     suma += pares
#     producto *= pares

# print("La suma de los números pares entre 20 y 500 es:", suma)
# print("El producto de los números pares entre 20 y 500 es:", producto)

# 3. Leer un lote de 475 valores de a uno por vez. Determinar y emitir el valor máximo del conjunto y el orden en que fue leído.
# Si hay más de un máximo considerar solo el primer valor hallado.

# max = 0

# for lote in range(475):
#   valor = int(input("Ingrese un valor"))
#   if valor > max:
#     max = valor
#   print("valor maximo ingresado es:",max)

# 4. Ingresar un Nº y un carácter y mostrar dicho carácter repetido tantas veces como indica el Nº.

# caracter= input("ingrese un caracter: ")
# numero = int(input(f"ingrese la cantidad de veces a repetir: {caracter}  ->"))

# for item in range(numero):
#   print(caracter)

# 5. Hacer un programa que lea 100 Números, indique cuáles son múltiplos de 2 y contarlos.

# contador = 0
# for valor in range(10):
#   numero = int(input(f"Ingrese el numero { valor+1 } : "))
#   if (numero % 2) == 0 :
#     print(numero)
#     contador+=1


# print("La cantidad de numeros multiplos de 2 es: ",contador)


# 6. Hacer un programa que lea 8 caracteres e indique que cantidad de ‘*’ y que cantidad de letras ‘a’ aparecen.

# asteriscos = 0
# letras_a = 0
# for caracter in range(8):
#   caracter = input("ingrese un caracter: ")
#   if caracter == "*":
#     asteriscos +=1
#   if caracter == "a":
#     letras_a +=1

# print("asteriscos ingresados: ",asteriscos)
# print("letras a ingresadas: ",letras_a)

# 7. ¿A cuánto asciende la suma de los números pares comprendidos entre 300 y 1232?


# suma = 0

# for pares in range(300, 1232, 2):
#     suma += pares

# print("La suma de los números pares entre 300 y 1232 asciende a :", suma)

# 8. Se efectúa una encuesta entre 1200 usuarios de sistemas operativos.
# Las respuestas están codificadas como 1, 2 o 3 según sea el elegido.
# Preparar un algoritmo para ingresarle las 1200 respuestas, y muestre por pantalla el número del sistema preferido.

# eleccion_1 = 0
# eleccion_2 = 0
# eleccion_3 = 0

# for respuestas in range(1200):
#     respuesta = int(input("Ingrese su votación (1-2-3): "))
#     if respuesta == 1:
#         eleccion_1 += 1
#     elif respuesta == 2:
#         eleccion_2 += 1
#     elif respuesta == 3:
#         eleccion_3 += 1

# # Determinar cuál fue la opción más elegida
# maximo_votos = max(eleccion_1, eleccion_2, eleccion_3)
# sistema_operativo = ""

# if eleccion_1 == maximo_votos:
#     sistema_operativo = "Sistema operativo 1"
# elif eleccion_2 == maximo_votos:
#     sistema_operativo = "Sistema operativo 2"
# else:
#     sistema_operativo = "Sistema operativo 3"

# print("El sistema operativo más elegido fue:", sistema_operativo, "con", maximo_votos, "votos.")


# 9. Desarrollar un algoritmo que determine en un conjunto de 100 números:
# a) Cuántos son mayores que 15.
# b) Cuántos son mayores que 50.
# c) Cuántos están comprendidos entre 25 y 45.

# mayores_que_15 = 0
# mayores_que_50 = 0
# entre_25_y_45 = 0

# for _ in range(100):
#     numero = int(input("Ingrese un número: "))
#     if numero > 15:
#         mayores_que_15 += 1
#     if 25 <= numero <= 45:  # Comprobamos si el número está entre 25 y 45
#         entre_25_y_45 += 1
#     if numero > 50:ñ
#         mayores_que_50 += 1

# print("Numeros mayores que 15:", mayores_que_15)
# print("Numeros entre 25 y 45:", entre_25_y_45)
# print("Numeros mayores que 50:", mayores_que_50)


# 10. Obtener un algoritmo que permita calcular la siguiente serie: h(n)=1 + ½ + 1/3 + ... +  1/n

# numero = int(input("Ingrese un número: "))
# serie = 1  # Comenzamos con el primer término de la serie (1)

# for num in range(2, numero + 1):  # Empezamos desde 2 ya que el primer término ya está incluido
#     serie += 1 / num

# print("El resultado de la serie es:", serie)


# 11. Se leen 50 pares de Números, c/u de los cuales tienen 2 valores: x e y distintos.
# • Se pide contar en cuantos pares x>y y en cuantos y>x.

# mayor_x = 0
# mayor_y = 0
# for item in range(50):
#   x= int(input("ingrese el valor x: "))
#   y= int(input("ingrese el valor y: "))
#   if x > y:
#     mayor_x+=1
#   if y > x:
#     mayor_y+=1

# print("cantidad de pares donde x > y: ",mayor_x)
# print("cantidad de pares donde y > x: ",mayor_y)


# 12. En un colegio de 1000 se ha registrado un código señalando el comportamiento académico de cada alumno.
# • Dicho código puede tomar valores 1, 2 o 3.
# • Indicar cuántos alumnos obtuvieron cada una de las calificaciones tratando de a una calificación por vez.

# calificacion_1 = 0
# calificacion_2 = 0
# calificacion_3 = 0

# for alumnos in range(10):
#     calificacion = int(input(f"Ingrese la calificación del alumno {alumnos}: "))
#     if calificacion == 1:
#         calificacion_1 += 1
#     elif calificacion == 2:
#         calificacion_2 += 1
#     elif calificacion == 3:
#         calificacion_3 += 1
#     else:
#         print("Ha ingresado una calificación incorrecta para el alumno", alumnos)

# print("Cantidad de alumnos con calificación 1:", calificacion_1)
# print("Cantidad de alumnos con calificación 2:", calificacion_2)
# print("Cantidad de alumnos con calificación 3:", calificacion_3)


# 13. En una fábrica hay 4.000 obreros distribuidos en cinco secciones.
# • Se requiere determinar cuántos obreros hay y el promedio de edad de los mismos por cada sección.
# • Asumir que se tiene como entrada los siguientes datos para cada obrero: Nº de empleado, sección a la que pertenece y edad.

# seccion_1 = 0
# seccion_2 = 0
# seccion_3 = 0
# seccion_4 = 0
# seccion_5 = 0
# total_edades_seccion_1 = 0
# total_edades_seccion_2 = 0
# total_edades_seccion_3 = 0
# total_edades_seccion_4 = 0
# total_edades_seccion_5 = 0

# for obrero in range(1, 4001):
#     numero_de_empleado = int(input(f"Ingrese el número de empleado para el obrero {obrero}: "))
#     seccion_fabrica = int(input(f"Ingrese la sección a la que pertenece el obrero {obrero}: "))
#     edad_de_empleado = int(input(f"Ingrese la edad del obrero {obrero}: "))

#     if seccion_fabrica == 1:
#         seccion_1 += 1
#         total_edades_seccion_1 += edad_de_empleado
#     elif seccion_fabrica == 2:
#         seccion_2 += 1
#         total_edades_seccion_2 += edad_de_empleado
#     elif seccion_fabrica == 3:
#         seccion_3 += 1
#         total_edades_seccion_3 += edad_de_empleado
#     elif seccion_fabrica == 4:
#         seccion_4 += 1
#         total_edades_seccion_4 += edad_de_empleado
#     elif seccion_fabrica == 5:
#         seccion_5 += 1
#         total_edades_seccion_5 += edad_de_empleado
#     else:
#         print(f"Se ingresó una sección inválida para el obrero {obrero}")

# # Calcular el promedio de edad por sección
# promedio_seccion_1 = total_edades_seccion_1 / seccion_1
# promedio_seccion_2 = total_edades_seccion_2 / seccion_2
# promedio_seccion_3 = total_edades_seccion_3 / seccion_3
# promedio_seccion_4 = total_edades_seccion_4 / seccion_4
# promedio_seccion_5 = total_edades_seccion_5 / seccion_5

# print(f"Cantidad de obreros en la sección 1: {seccion_1}, promedio de edad: {promedio_seccion_1}")
# print(f"Cantidad de obreros en la sección 2: {seccion_2}, promedio de edad: {promedio_seccion_2}")
# print(f"Cantidad de obreros en la sección 3: {seccion_3}, promedio de edad: {promedio_seccion_3}")
# print(f"Cantidad de obreros en la sección 4: {seccion_4}, promedio de edad: {promedio_seccion_4}")
# print(f"Cantidad de obreros en la sección 5: {seccion_5}, promedio de edad: {promedio_seccion_5}")

# 14. Construir un algoritmo que muestre por pantalla las tablas de multiplicar usuales hasta el Nº 10.
# •  Ej: 5 por 1 es 5
# •  5 por 2 es 10
# •  5 por 3 es 15


# for num1 in range(1,11):
#   for num2 in range(11):
#     print(f"{num1} X {num2} = {num1*num2}")
#   print("")

# 15. Construir un algoritmo que muestre por pantalla las tablas de multiplicar usuales para valores comprendidos entre a y b. (a<b).

# primero = int(input("Ingrese el primer valor: "))
# segundo = int(input("Ingrese el segundo valor: "))

# #  Nos aseguramos que el primer valor sea menor que el segundo
# if primero >= segundo:
#     print("Error: El primer valor debe ser menor que el segundo.")
# else:
#     for num1 in range(primero, segundo + 1):
#         print(f"Tabla de multiplicar del {num1}:")
#         for num2 in range(11):
#             print(f"{num1} x {num2} = {num1*num2}")
#         print("")  # Imprimir línea en blanco para separar las tablas


# 16. Dada una secuencia de caracteres acabada en #, mostrar los números (0..9) que en  ella aparecen.

# print("Ingrese cualquier caracter a continuacion, Ingrese # para salir del ciclo...")
# contador_numeros = 0
# caracter = ""
# while caracter != "#":
#   caracter = input("Ingrese un caracter: ")
#   if caracter.isdigit():
#     contador_numeros+=1

# print("La cantidad de numero del 0..9 ingresados es: ",contador_numeros)


# 17. Construir un algoritmo que, dada una secuencia de enteros acabada con el valor cero, devuelva el mayor de ellos.
# • Determinar cuántos números negativos han aparecido.

# print("Ingrese cualquier numero a continuacion, Ingrese 0 para salir del ciclo...")
# contador_negativos = 0
# mayor = 0
# numero = ""
# while numero != 0:
#   numero =  int(input("Ingrese un numero: "))
#   if numero < 0:
#     contador_negativos+=1
#   elif numero > mayor:
#     mayor = numero

# print("El mayor numero  ingresado es: ",mayor)
# print("La cantidad de numeros negativos ingresados es: ",contador_negativos)


# 18. Dada una secuencia de caracteres acabada en punto:
# •  obtener un algoritmo que determine cuantas veces aparece un determinado carácter, el cual será leído previamente.

# contador = 0
# caracter = input("Ingrese un caracter previo: ")
# consulta = ""
# while consulta != ".":
#   consulta = input("Ingrese un caracter: ")
#   if consulta == caracter:
#     contador+=1

# print(f" '{caracter}' fue ingresado {contador} veces")


# 19. Contar la cantidad de Números negativos de una lista que finaliza con el Nº 0.

# print("Ingrese cualquier numero a continuacion, Ingrese 0 para salir del ciclo...")
# contador_negativos = 0
# numero = ""
# while numero != 0:
#   numero =  int(input("Ingrese un numero: "))
#   if numero < 0:
#     contador_negativos+=1


# print("La cantidad de numeros negativos ingresados es: ",contador_negativos)

# 20. Escribir un algoritmo que permita leer una serie de enteros. Contar el Nº de valores introducidos y su suma.

# print("Ingrese cualquier numero a continuacion, Ingrese 0 para salir del ciclo...")
# acumulador = 0
# contador = 0
# numero = ""
# while numero != 0:
#   numero =  int(input("Ingrese un numero: "))
#   acumulador+=numero
#   contador+=1

# print(f"La cantidad de numeros ingresados es: {contador}  su suma es {acumulador}")

# 21. Se dispone de un mazo de cartas españolas. Se debe sacar la primera carta y separarla.
# • Luego sacar de a una carta por vez hasta encontrar una del mismo palo y número mayor a la primera.
# • El problema planteado es determinar cuántas cartas fue necesario extraer del mazo.

# carta_separada = int(input("Ingrese el número de la primer carta: "))
# palo_separado = input("Ingrese el palo de la primer carta: ")
# carta = 0
# palo = ""
# contador = 0

# while True:
#     palo = input("Ingrese el palo de la siguiente carta (o 'exit' para terminar): ")
#     if palo.lower() == 'exit':
#         break
#     carta = int(input("Ingrese el número de la siguiente carta: "))
#     contador += 1

#     if palo == palo_separado and carta > carta_separada:
#         break

# print(f"Fue necesario extraer {contador} cartas para salir del ciclo.")


# 22. Dada una lista de valores numéricos, hallar su rango, es decir la diferencia entre su valor máximo y su valor mínimo.

# valor = int(input("Ingrese un número: "))
# minimo = valor
# maximo = valor

# while True:
#     valor = int(input("Ingrese un número: "))

#     if valor > maximo:
#         maximo = valor
#     elif valor < minimo:
#         minimo = valor

#     condicion = input("¿Desea salir? (si/no): ")
#     if condicion.lower() == "si":
#         rango = maximo - minimo
#         print("El rango es:", rango)
#         break


# 23. Dada una lista de valores enteros positivos, hallar cuántos valores mayores que 1.000 hay.
# • Si la cantidad es menor que 20 calcular su factorial.

# contador = 0
# while True:
#   valor = int(input("Ingrese un valor: "))
#   if valor > 1000:
#       contador+=1

#   condicion = input("¿Desea salir? (si/no): ")
#   if condicion.lower() == "si":
#       break

# if contador <20:
#   factorial = 1
#   if contador == 0:
#     print("El factorial de 0 es 1.")
#   else:
#     for i in range(1, contador + 1):
#         factorial *= i
#     print("El factorial de", contador, "es", factorial)


# 24. Se dispone de un conjunto de tarjetas rojas y azules, las cuales están numeradas en forma correlativa.
# • El lote de tarjetas termina con una tarjeta blanca.
# • El problema es determinar de las tarjetas del lote:
# • cuántas son azules y con número par; cuántas son rojas y con número impar, y cuántas son las restantes (excepto la blanca).

# contador_total = 0
# rojas_impares = 0
# azules_pares = 0

# while True:
#   tarjeta = input("Ingrese una tarjeta: ")
#   if tarjeta == "blanca":
#     break
#   contador_total+=1;
#   if contador_total % 2 != 0 and tarjeta == "roja":
#     rojas_impares+=1
#   elif contador_total % 2 ==0 and  tarjeta == "azul":
#     azules_pares+=1

# print(f"Cantidad de tajetas azules pares: {azules_pares}")
# print(f"Cantidad de tajetas rojas  impares: {rojas_impares}")
# print(f"Cantidad de tajetas restantes: {contador_total-(rojas_impares+azules_pares)-1}")

# 25. Dada una lista de precios de productos, la cual termina con un precio igual a cero.
# •Se desea saber el monto total a pagar y la cantidad de artículos comprados.

# monto_total = 0
# contador_productos = 0

# while True:
#     precio = int(input("Ingrese el precio del producto: $"))
#     if precio == 0:
#         break
#     contador_productos += 1
#     monto_total += precio


# print(f"Usted compro {contador_productos} productos, por un total de ${monto_total}")


# 26. Tenemos una empresa que necesita incorporar a su plantilla varios empleados en diversos departamentos.
#  Se reciben multitud de Currículum Vitae y se intenta introducir en una pequeña aplicación para realizar una primera selección
#  y en base a su resultado, comprobaremos si es apto o no apto para optar al cargo.
# Necesita la empresa:
# Un administrativo.
# Un transportista.
# Dos operarios.
# Tres guardias de seguridad.
# • Para todos los puestos tienen que tener 18 años
# • Para administrativo y transportista pueden tener hasta 55 años.
# • Para operarios no pueden superar los 50 años.
# • Para guardia de seguridad no pueden superar los 45 años.
# • Para administrativo se requiere el Ciclo superior en Administración y Finanzas.
# • Para los demás puestos el titulo secundario.
# Una vez haya superado los requerimientos anteriores, introduciremos el nombre, apellidos, dirección y número de DNI.

# mensaje_rechazo = "lo siento usted no cumple con los requisitos de la empresa"

# while True:
#     print("Bienvenido al programa de seleccion de STAR LIQUID CLOUDS")
#     print("Las politicas de la empresa tienen un riguroso filtrado relativo a su edad ")
#     edad = int(input("por favor ingrese su edad: "))
#     if edad < 18 or edad > 55:
#         print(mensaje_rechazo)
#         break
#     else:
#         condicion = input("¿Posee titulo secundario? si/no: -->  ").lower()
#         if condicion == "no":
#             print(mensaje_rechazo)
#             break
#         else:
#             if edad < 45:
#                 opciones = "• 1 --> Administrativo\n• 2 --> Transportista\n• 3 --> Operario\n• 4 --> Guardia de seguridad"
#             elif edad < 50:
#               opciones = "• 1 --> Administrativo\n• 2 --> Transportista\n• 3 --> Operario"
#             elif edad < 55:
#                 opciones = "• 1 --> Administrativo\n• 2 --> Transportista"


#         while True:
#           print (f"Teniendo en cuenta sus {edad} años, usted puede postularse para:\n{opciones}")
#           respuesta = int(input("\nIngrese el número del puesto al que desea aplicar: "))
#           if edad < 45:
#               if respuesta == 1:
#                   trabajo = "Administrativo"
#                   break
#               elif respuesta == 2:
#                   trabajo = "Transportista"
#                   break
#               elif respuesta == 3:
#                   trabajo = "Operario"
#               elif respuesta == 4:
#                   trabajo = "Guardia de seguridad"
#                   break
#               else:
#                   print("Parece que ingresó una opción no válida.")
                  
#           elif edad < 50:
#               if respuesta == 1:
#                   trabajo = "Administrativo"
#                   break
#               elif respuesta == 2:
#                   trabajo = "Transportista"
#                   break
#               elif respuesta == 3:
#                   trabajo = "Operario"
#                   break
#               else:
#                   print("Parece que ingresó una opción no válida.")
                  
#           elif edad < 55:
#               if respuesta == 1:
#                   trabajo = "Administrativo"
#                   break
#               elif respuesta == 2:
#                   trabajo = "Transportista"
#                   break
#               else:
#                   print("Parece que ingresó una opción no válida.")
                  

#         print(f"Usted aplicó para el trabajo de {trabajo} \n")
#         if trabajo == "Administrativo":
#           condicion = input("¿ posee Ciclo superior en Administración y Finanzas ?  si/no--> ").lower()
#           if condicion =="no":
#               print(mensaje_rechazo)
#               break
#           else:
#             nombre = input("Ingrese su nombre: ")
#             apellido = input("Ingrese su apellido: ")
#             direccion = input("Ingrese su dirección: ")
#             dni = input("Ingrese su DNI: ")
#             print(f"\nFelicitaciones {nombre} {apellido} usted ha sido contratado como {trabajo} !!! ansiamos su presencia en nuestro espacio ")
#             break    
#         else:
#           nombre = input("Ingrese su nombre: ")
#           apellido = input("Ingrese su apellido: ")
#           direccion = input("Ingrese su dirección: ")
#           dni = input("Ingrese su DNI: ")
#           print(f"\nFelicitaciones {nombre} {apellido} usted ha sido contratado como {trabajo} !!! ansiamos su presencia en nuestro espacio ")
#           break