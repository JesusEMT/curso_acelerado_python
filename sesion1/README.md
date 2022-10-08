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
