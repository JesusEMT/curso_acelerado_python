'''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion2/ejercicio8.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: detecte, números positivos, negativos y cero
'''
numero = int(input("Escriba un número: "))
if (numero == 0): 
  print("El numero",numero, " es cero")
elif (numero > 0): 
  print("El numero",numero, "es positivo ")
elif (numero < 0): 
  print("El numero",numero, "es negativo")


'''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion2/ejercicio9.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: preguntar contraseña a usuario y la comparar con valor registrado
'''
contra = (input("Escriba su contraseña : "))
password = ("contra1234")

if (password != contra): 
  print("Error la contraseña es incorrecta")
  
  
  '''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion2/ejercicio10.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: numero par o impar
'''
n = int(input("Introduce un número entero: "))
if n % 2 == 0:
  print("El número " + str(n) + " es par")
else:
  print("El número " + str(n) + " es impar")
  
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
  
  
  '''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion2/ejercicio12.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: estructura condicional anidada
'''
mes = int(input("Introduzca el mes de año: "))
if 1 <= mes <= 12:
  print("Se ha introducido un mes válido.")
else:
  print("El mes es incorrecto. Por defecto se elige Enero.")
  mes = 1
  print("Se utilizará mes", mes)
