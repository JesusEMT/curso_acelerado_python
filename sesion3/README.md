'''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio13.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: suma de 10 primeros numeros
'''
num = 1
suma = 0
while num <= 10:
  suma += num
  print(suma)
  num += 1
  
  
  '''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio14.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: repetir palabra 10 veces
'''

num = 0 
palabra = input ("Ingrese una palabra: ")
while num<10:
  print(palabra)
  num += 1
  
  
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
