# LABORATORIO 01 (Simulacro)

## Descripción General
El siguiente laboratorio consiste en una serie de ejercicios para practicar el desarrollo de programación en **sintaxis de Python**, además de evaluación de conceptos vistos en clases anteriores.
El objetivo de este laboratorio está en el uso de la **condicional IF**, **creación de funciones**, recuerde que en cada función que desarrollen agregar los **comentarios** (nombre, parámetros entrada, salida y restricciones), además, se reforzará el uso de los **inputs** para el manejo de menú.
Finalizado el laboratorio subir el archivo con el nombre de **Laboratorio01.py**, la entrega cierra a las **3pm del 24 de febrero del 2022** y será a través del Github Classroom

## Ejercicio 1. Valor 7 puntos.
Escriba una función llamada **division(dividendo, divisor) **
Sus parámetros de entrada deben ser:
-	Tipo Entero.
-	No negativos
-	De tomar en cuenta de que, si se divide entre cero, debe mostrar ese mensaje de que no es permitido
-	El divisor no debe ser mayor que el dividendo

El resultado debe ser la división entre el dividendo y el divisor

``` python
>>> division(10, 2)
5
>>> division(0, 2)
0
>>> division(10, 10)
1
>>> division(10, 15)
“Error: El divisor es mayor que el dividendo”
>>> division(10, 0)
“Error: La división entre CERO no es permitido”
>>> division(10, -5)
“Error: Uno de los parámetros es negativo”
``` 

## Ejercicio 2. Valor 3 puntos.
Escriba una función llamada **divisionVersion2()** 
Sus parámetros de entrada deben ser:
-	El dividendo y divisor será haciendo uso **INPUT**
-	Tipo Entero.
-	No negativos
-	De tomar en cuenta de que, si se divide entre cero, debe mostrar ese mensaje de que no es permitido
-	El divisor no debe ser mayor que el dividendo

``` python
>>> división() #0, 2
5
>>> division() #0, 2
0
>>> division() #10, 10
1
>>> division() #10, 15
“Error: El divisor es mayor que el dividendo”
>>> division() #10, 0
“Error: La división entre CERO no es permitido”
>>> division() #10, -5
“Error: Uno de los parámetros es negativo”
``` 

## Ejercicio 3. Valor 10 puntos.
Escriba una función llamada **calculoIVA(tipoServicio, monto)**
Sus parámetros de entrada deben ser:
-	El valor de tipoServicio puede ser 1, 2 o 3, si es diferente a estos valores enteros debe mostrar su mensaje de error
-	Ambos parámetros deben ser tipo Entero.
-	Además, No negativos
-	Si el valor de tipoServicio es:
  -	1, se calcula el impuesto con 13%
  - 2, se calcula el impuesto con 2%
  - 3, se calcula el impuesto con 6%

El resultado debe ser el monto más el impuesto de IVA calculado

``` python
>>> calculoIVA(1, 1000)
1130
>>> calculoIVA(2, 1000)
1020
>>> calculoIVA(3, 1000)
1060
>>> calculoIVA(5, 1000)
“Error: El valor de tipoServicio debe ser 1, 2 o 3”
>>> calculoIVA(1, 1000.5)
“Error: Un parámetro no es de tipo Entero”
>>> calculoIVA(1, -1000)
“Error: Uno de los parámetros es negativo”
``` 
