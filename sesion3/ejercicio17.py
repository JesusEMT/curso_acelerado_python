'''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio17.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: Tablas de multiplicar
'''
tabla = int (input("Numero de la tabla de multiplicar "))
i = 1
while (i <=12):
  if (i<10):
    print (i,"  x "," = ", tabla*i )
    i+=1
  else:
    print (i," x "," = ", tabla*i )  
    i+=1
