'''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio16.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: imprime un triangulo
'''
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n): 
  for j in range(i + 1):  
    espacio=n-i
  print(" "*espacio," *"*i)
  print("")