''''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion4/ejercicio19.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: invertir la palabra usando listas y funcion reverse()
'''

word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
  print("Es un palíndromo")
else:
  print("No es un palíndromo")