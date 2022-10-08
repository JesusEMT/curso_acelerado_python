''''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio22.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: Ingresar numeros en lista y ordenar de mayor a menor
'''


num_ganador=[]
for i in range(5):
  num_loteria = int( input("Ingrese numeros ganadores de loteria: "))
  num_ganador.append(num_loteria)
num_ganador.sort()
print(num_ganador)
