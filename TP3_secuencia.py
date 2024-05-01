# TRABAJO PRÁCTICO Nº 3 SECUENCIA.

from math import sqrt,pi # como se usan operaciones con raices cuadradas fue pertinente importar la funcion "sqrt" del modulo "math"


# 1. Leer tres números de a una por vez, calcular su suma y su producto.

# numero1= int(input("ingrese numero 1: ")) # se convierten los inputs a enteros porque por defecto son strings
# numero2= int(input("ingrese numero 2: ")) # se convierten los inputs a enteros porque por defecto son strings

# suma = numero1+numero2
# producto = numero1*numero2

# print("suma: ",suma)
# print("producto: ",producto)

# 2. Dadas las longitudes de los dos catetos de un triángulo rectángulo, hallar la longitud de la hipotenusa:

# longitud1= int(input("ingrese longitud 1: ")) # se convierten los inputs a enteros porque por defecto son strings
# longitud2= int(input("ingrese longitud 2: ")) # se convierten los inputs a enteros porque por defecto son strings

# hipotenusa = sqrt(longitud1**2+longitud2**2)
# print("hipotenusa: ",hipotenusa)


# 3.	Dadas las horas trabajadas por un operario y el valor de las mismas, determinar que sueldo percibe dicho operario. 
# Se solicita indicar cuanto cobraría si se aplican descuentos del 20%

# cantidad_horas= int(input("Horas Trabajaads: ")) # se convierten los inputs a enteros porque por defecto son strings
# valor_horas= int(input("Valor de cada hora : ")) # se convierten los inputs a enteros porque por defecto son strings

# sueldo = cantidad_horas*valor_horas
# print("Sueldo: $",sueldo)
# print("Sueldo con descuento del 20%: $",sueldo-sueldo*0.2)

# 4. Hallar el área de un cuadrado, cuyos lados tienen la longitud de la hipotenusa de un triángulo rectángulo y cuyos catetos son dados.

# cateto1= int(input("ingrese cateto 1: ")) # se convierten los inputs a enteros porque por defecto son strings
# cateto2= int(input("ingrese cateto 2: ")) # se convierten los inputs a enteros porque por defecto son strings

# hipotenusa = sqrt(cateto1**2+cateto2**2)
# print("area: ",hipotenusa**2)


# 5. Dadas las calificaciones de 4 exámenes finales de un estudiante determinar el promedio.

# calificacion1= int(input("ingrese calificacion 1: ")) # se convierten los inputs a enteros porque por defecto son strings
# calificacion2= int(input("ingrese calificacion 2: ")) # se convierten los inputs a enteros porque por defecto son strings
# calificacion3= int(input("ingrese calificacion 3: ")) # se convierten los inputs a enteros porque por defecto son strings
# calificacion4= int(input("ingrese calificacion 4: ")) # se convierten los inputs a enteros porque por defecto son strings

# suma_de_calificaciones = calificacion1+calificacion2+calificacion3+calificacion4
# promedio = suma_de_calificaciones/4
# print("su promedio final: ",promedio)



# 6. Diseñe un algoritmo que determine el porcentaje de: 
  #• Alumnos promocionados, Alumnos regularizados, Alumnos desaprobados y Alumnos libres, 
  #• teniendo como datos cantidad de alumnos que cumplen con cada condición.

# promocionados = int(input("ingrese Cantidad de Alumnos  promocionados: ")) 
# regularizados = int(input("ingrese Cantidad de alumnos regularizados: "))  
# desaprobados = int(input("ingrese Cantidad de alumnos desaprobados: "))    
# libres = int(input("ingrese Cantidad de alumnos libres: "))                

# alumnos_totales = promocionados+regularizados+desaprobados+libres

# print("cantidad total de alumnos",alumnos_totales)
# print("porcentaje de alumnos  promocionados",(promocionados*100)//alumnos_totales,"%")
# print("porcentaje de alumnos  regularizados",(regularizados*100)//alumnos_totales,"%")
# print("porcentaje de alumnos  desaprobados",(desaprobados*100)//alumnos_totales,"%")
# print("porcentaje de alumnos  libres",(libres*100)//alumnos_totales,"%")


# 7. Dados dos números a y b, se desea intercambiar sus valores, utilizando una variable auxiliar.

# numero_a = int(input("ingrese numero a: ")) 
# numero_b = int(input("ingrese numero b: "))  

# auxiliar = 0
# print("numero a antes: ",numero_a) 
# print("numero b antes: ",numero_b) 

# auxiliar = numero_a
# numero_a = numero_b
# numero_b = auxiliar

# print("numero a despues: ",numero_a)
# print("numero b despues: ",numero_b)


# 8. Escribir un programa que lea dos números enteros A y B, y obtenga los valores A div B, A mod B.

# numero_a = int(input("ingrese numero a: ")) 
# numero_b = int(input("ingrese numero b: "))  

# print("A div B: ",numero_a//numero_b) 
# print("A mod B: ",numero_a%numero_b)  



# 9.	Dado el número matemático PI: 
# Se solicita al usuario que ingrese el valor del radio de una circunferencia y calcule y muestre por pantalla el área y perímetro. 
# (área = PI * radio^2) (perímetro = 2PI * radio)


# radio = float(input("Ingrese el radio de una circunferencia: "))

# area = pi * radio**2 
# perimetro = 2*pi * radio
# 6
# print("Area: ",area)
# print("Perimetro: ",perimetro)



# 10.	Solicitar al usuario que ingrese:
# El precio de un producto al inicio del año, y el precio del mismo producto transcurrido un determinado tiempo. 
# El usuario debe mostrar cuál fue el porcentaje de aumento que tuvo ese producto en el año.

# precio_inicial = float(input("Precio Inicial: "))
# precio_posterior = float(input("Precio Posterior: "))

# diferencia= (precio_posterior-precio_inicial)
# porcentaje =  (diferencia/precio_inicial)*100

# print("El producto aumento un %",porcentaje)



# 11.	De los y las estudiantes de Fundamentos de Programación se desea saber:
# Qué porcentaje de personas menores a 20 años se encuentran cursando la materia. 
# El programa debe solicitar al usuario que ingrese la cantidad total de estudiantes menores a 20 años y el total.

# estudiantes_menores = int(input("Estudiantes menores de 20 años: "))
# total_estudiantes = int(input("Total de estudiantes: "))

# porcentaje = (estudiantes_menores/total_estudiantes)*100

# print("Porcentaje de menores a 20 años cursando: %",porcentaje)


# 12. Un millonario excéntrico tenía tres hijos: Carlos, José y Marta. Al morir dejó el siguiente legado: 
#• A José le dejó 4/3 de lo que le dejó a Carlos. A Carlos le dejó 1/3 de su fortuna.
#• A Marta le dejo la mitad de lo que le dejó a José. 
#• Preparar un algoritmo para darle la suma a repartir e imprima cuanto le tocó a cada uno

# legado = int(input("ingrese el legado del millonario excentrico: ")) 
# herencia_carlos = legado//3
# herencia_jose = (4*herencia_carlos)//3
# herencia_marta = (herencia_jose//2)

# print("La herencia que le corresponde a  carlos es: $",herencia_carlos)
# print("La herencia que le corresponde a  jose es: $",herencia_jose)
# print("La herencia que le corresponde a  marta es: $",herencia_marta)