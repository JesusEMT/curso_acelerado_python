''''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio23.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: Tuplas, producto escalar de vectores
'''
a = (1, 2, 3)
b = (-1,0, 2)
c = (-2, 6, 7)
product = 0
for i in range(len(a)):
  product += a[i]*b[i]*c[i]
print("El producto de los vectores:","\n"+" "*7+str(a),"\n"+" "*7+str(b) + " = " + str(product),"\n"+" "*7+str(c))