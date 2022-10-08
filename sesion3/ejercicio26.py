''''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio26.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: Diccionario con {'Euro':'€', 'Dolar':'US$', 'Peso':’$'} y y monstrar simbolo
'''
divisa = {'Euro':'€', 'Dolar':'US$', 'Peso':'$'}
simbolo = input("Introduzca una divisa: ")
if simbolo.title() in divisa:
    print("Su simbolo es: "+divisa[simbolo.title()])
else:
    print("La divisa no esta en el diccionario.")