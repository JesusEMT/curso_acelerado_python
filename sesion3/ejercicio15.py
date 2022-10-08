'''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio15.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: suma valores ingresados por teclado
'''

suma = 0
for f in range(10):
  valor = int(input("Ingrese valor: "))
  suma += valor
print("La suma es", suma)
promedio = suma / 10
print("El promedio es: ", promedio)
