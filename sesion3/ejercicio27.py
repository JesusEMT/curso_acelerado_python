''''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio27.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: Preguntar al usuario su nombre, edad, dirección y teléfono y lo guardar en un diccionario y despues mostrar por pantalla
'''

datos={'nombre','edad','direccion','telefono'}
nombre = input('¿Cual es tu nombre? ')
edad = input('¿Cual es tu edad? ')
direccion = input('¿Cual es tu direccion? ')
telefono = input('¿Cual es tu numero de telefono?')
datos = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(" ")
for clave,valor in datos.items(): 
     print ("%s es %s" % (clave, valor))



