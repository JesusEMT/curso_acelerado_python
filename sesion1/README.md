'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion1/ejercicio1.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: Asignación de variables
'''
nombre_estado = 'Tabasco'
superficie = 25267
poblacion_total = 2403000000
promedio_temperatura = 31.3
estados_cercanos = ['chiapas','campeche','veracruz']
productos_tabasco=['Cacao', 'Coco', 'Caña']
print(nombre_estado, " es un estado que ", )
print("con ",estados_cercanos[0], "colinda al sur", ",")
print("tiene una superficie de ", superficie,",")
print("tiene una temperatura de ", promedio_temperatura,'y')
print("es productor de ", productos_tabasco[0])


'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion1/ejercicio2.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: superficie de un cuadrado
'''
lado=input("Ingrese la medida del lado del cuadrado:")
lado=float(lado)
superficie=lado*lado
print("La superficie del cuadrado es")
print(superficie)


'''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion1/ejercicio3.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: pago de trabajador
'''
horas = float(input("Introduce tus horas de trabajo: "))
horas_extra = float(input("Introduce tus horas extra de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = (horas+horas_extra) * coste
print("Tu paga es", paga)


'''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion1/ejercicio4.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: indice de masa corporal peso en kg/ estatura mtrs cuadrados
'''
peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))


'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion1/ejercicio5.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: conversion de temperatura
'''
celsius=input("Ingrese la temperatura en grados Celsius:")
celsius=float(celsius)
fahrenheit=((celsius*1.8)+(32))
print("La temperatura en grados Fahrenheit es:",fahrenheit)


'''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion1/ejercicio6.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: imprime capital obtenido de una inversión
'''
cantidad = float( input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))

'''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion1/ejercicio6.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: Suma de los primeros números enteros
'''
n = int(input("Introduce un número entero: "))
suma = n * (n + 1) / 2
print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))
