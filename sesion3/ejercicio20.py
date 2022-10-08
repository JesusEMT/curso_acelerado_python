''''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio20.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: almacenar precios y ordenar de mayor a menor
'''

prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
  if price < min:
    min = price
  elif price > max:
    max = price
print("El mínimo es " + str(min))
print("El máximo es " + str(max))
listSum = sum(prices)
print(f"La suma es de toda la lista es {listSum}")