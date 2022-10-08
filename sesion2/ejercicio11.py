'''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion2/ejercicio11.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: estructura condicional anidada
'''
mes = int(input("Introduzca el mes del año: "))
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 11:
  print("El mes tiene 31 días.")
elif mes == 2:
  print("El mes tiene 28 o 29 días.")
elif mes == 4 :
  print("El mes tiene 30 días.")
else:
  print("Mes no válido.")