## TRABAJO PRÁCTICO Nº 1 ENTENDER EL PROBLEMA.

_❗❗ Se asume aqui que el objetivo del trabajo practico N°1 es definir los pasos necesarios y para resolver los problemas, y estructurar los pasos adecuadamente..._

1.	Dado el número matemático PI, se solicita al usuario que ingrese el valor del radio de una circunferencia y calcule y muestre por pantalla el área y perímetro. (área = PI * radio2) (perímetro = 2 * PI * radio.)

### Resolucion:

#### Paso 1:
+ Se pide el dato al usuario
+ Una vez que este ingresa el dato se verifica que no sea negativo, el radio no puede ser negativo.
+ Si el radio es positivo, entonces se procede al paso 2.

#### Paso 2:
+ Con el dato del usuario se realizan los calculos y se almacenan en variables diferentes llamadas "area" y "perimetro" (las variables van a guardar datos numericos, puntualmente numeros reales)

#### Paso 3:
+ Una vez calculados los valores y almacenados en las variables, se muestra el resultado al usuario.

2.	Dadas las longitudes de los dos catetos de un triángulo rectángulo, hallar la longitud de la hipotenusa.

### Resolucion:

#### Paso 1:
Debemos conocer los numeros exactos que vale cada cateto del triangulo rectangulo para poder hallar la hipotenusa.

#### Paso 2:
Una vez obtenidos estos debemos encontrar una formula que permita hallar la hipotenusa usando los catetos como datos.

#### Paso 3:
Una vez obtenida la formula aplicarla para obtener el valor  el hipotenusa

3.	Dadas las horas trabajadas por un operario y el valor de las mismas, determinar que sueldo percibe dicho operario.
### Resolucion:

#### Paso 1:
Es necesario conocer el Numero de horas que trabaja este operario, y tambien cuanto le pagan por cada una de esas horas.

#### Paso 2:
Una vez que tenemos estas dos cantidades, podemos multiplicarlas para obtener el resultado deseado.


4.	Ídem anterior, pero considerando que se le debe aplicar los descuentos correspondientes por ley: 
    los mismos son del 20%. Mostrar el sueldo a cobrar.

### Resolucion:

#### Paso 1:
Es necesario conocer el Numero de horas que trabaja este operario, y tambien cuanto le pagan por cada una de esas horas.

#### Paso 2:
Una vez que tenemos estas dos cantidades, podemos multiplicarlas para obtener el resultado el sueldo total.

#### Paso 3:
finalmente aplicamos un descuento estipulado al sueldo total, y reflejamos este valor.


5.	Dados dos valores A y B distintos, determinar cuál es el mayor.

### Resolucion:

#### Paso 1:
Necesitamo conocer el valor de A y el valor  de B

#### Paso 2:
Para poder determinar si un numero es mayor a otro es necesario que estos numeros sean distintos.

#### Paso 3:
Si la resta de A - B es un numero positivo significa que A es mayor a B , de lo contrario B es mayor a A


6.	Determinar si una palabra cualquiera es un palíndromo (capicúa); por ejemplo: Neuquén.

### Resolucion:

#### Paso 1:
Primero debemos comprender que una palabra palindroma se escribe igual en ambos sentidos.

#### Paso 2:
Para determinar si una palabra es palindroma o no, podemos invertir la palabra obtenida.

#### Paso 3:
Si la inversion de esta palabra es igual a la palabra original , entonces esta palabra es palindroma.


7.	Dadas las calificaciones de 4 exámenes finales de un estudiante determinar el promedio.

### Resolucion:

#### Paso 1:
Una vez sabidas las 4 notas del estudiantes.
#### Paso 2:
Podemos calcular su promedio dividiendo la suma total de los examens sobre el total de examenes rendidos
#### Paso 3:
Finalmente este valor lo podemos almacenar y mostrar.

8.	Dada una lista de 3 números determinar si el Nº 3 se encuentra en dicha lista.

### Resolucion:

#### Paso 1:
Primero Debemos conocer la lista de estos numeros.

#### Paso 2:
Una vez obtenida la lista, evaluamos si alguno de estos numeros es igual al numero 3

#### Paso 3:
Si alguno de estos numeros cumple esta condicion significa que el N° 3 , se encuentra en la lista.


9.	Calcular el valor a cancelar de un producto de un monto ingresado: 
    el programa debe mostrar cómo se presenta en una factura
    subtotal (cantidad por precio)
    IVA (del subtotal) y total a pagar 
    (la suma del subtotal + el IVA). IVA=21%.

### Resolucion:

Cálculo del total a pagar: Suma el subtotal y el IVA para obtener el total a pagar.
Presentación de resultados: Muestra al usuario el subtotal, el monto del IVA y el total a pagar.

#### Paso 1:
desde el principio podemos determinar que el IVA es un valor que no va a cambiar nunca.
Debemos adquirir el precio de cada producto, este puede ser un numero decimal.
Debemos adquirir la cantidad de productos disponibles que hay

#### Paso 2:
El subtotal se obtiene multiplicando la cantidad de productos pr el precio de cada producto.
Subtotal = cantidad x precio.

#### Paso 3:
Para calcular el IVA podemos multiplicar el subtotal x 0.21 , obteniendo una diferencia.
IVA = subtotal x 0.21

#### Paso 4:
Para obtener el total a pagar debemos sumar el aumento del IVA al subtotal:
Total = subtotal + IVA

#### Paso 5:
Finalmente mostramos todos los resultados generados en una factura:
mostramos: Subtotal,IVA,Total


10.	Escribir un programa que calcule el volumen de un cilindro. 
    Para ello se deberá solicitar al usuario que ingrese el radio y la altura. Mostrar el resultado por pantalla. 
    volumen = π * radio2 * altura.

### Resolucion:

#### Paso 1:
Primero debemos recolectar del usuario el radio y la altura ingresadas.
#### Paso 2:
Posteriormente implementamos la formula del volumen, la cual es:      volumen = π * radio2 * altura.
#### Paso 3:
Finalmente mostramos el resultado por pantalla.

11.	Solicitar al usuario que ingrese el precio de un producto al inicio del año, y el precio del mismo producto transcurrido un determinado tiempo. 
El usuario debe mostrar cuál fue el porcentaje de aumento que tuvo ese producto en el año.

### Resolucion:

#### Paso 1:
Primero le pedimos al usuario que ingrese el precio de un producto, cuando el año recien incia.
#### Paso 2:
Primero le pedimos al usuario que ingrese el precio de un producto, cuando ya haya transcurrido un tiempo.
#### Paso 3:
Para determinar el porcentaje de de aumento de una cantidad se debe usar la siguiente formula
Porcentaje de aumento= [(Valor inicial- Valor final) /  Valor inicial] x 100%
#### Paso 4:
Implementando la formula podemos determinar el porcentaje de aumento.
#### Paso 5:
Finalmente mostramos el resultado de la operacion por pantalla, explicandole al usuario que ese fue el porcentaje de aumento del producto

12.	De los y las estudiantes de Fundamentos de Programación se desea saber
    qué porcentaje de personas menores a 20 años se encuentran cursando la materia. 
    El programa debe solicitar al usuario que ingrese la cantidad total de estudiantes menores a 20 años y el total.

### Resolucion:

#### Paso 1:
primero debemos adquirir la cantidad total de estudiantes menores a 20 años
#### Paso 2:
segundo debemos adquirir la cantidad total de estudiantes
#### Paso 3:
Mediante la formula correcta podemos obtener que porcentaje representan los menores de 20 años:
porcentaje = (cantidad/total) x 100%
#### Paso 4:
Finalmente podemos mostrar el resultado al usuario:
