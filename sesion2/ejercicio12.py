'''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion/ejercicio12.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: estructura condicional anidada
'''
mes = int(input("Introduzca el mes de año: "))
if mes <=12 and mes >=1:
  print("Se ha introducido un mes válido.")
else:
  print("El mes es incorrecto. Por defecto se elige Enero.")
  mes = 1
  print("Se utilizará mes", mes)