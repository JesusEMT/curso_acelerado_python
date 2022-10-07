'''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion/ejercicio6.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: imprime capital obtenido de una inversión
'''
cantidad = float( input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))
