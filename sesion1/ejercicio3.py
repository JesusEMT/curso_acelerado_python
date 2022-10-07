'''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion/ejercicio3.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: pago de trabajador
'''
horas = float(input("Introduce tus horas de trabajo: "))
horas_extra = float(input("Introduce tus horas extra de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = (horas+horas_extra) * coste
print("Tu paga es", paga)