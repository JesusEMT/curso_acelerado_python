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


''''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio18.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: Personas autorizadas
'''
personas_autorizadas = ["Alberto", "Carmen", "Jesus"]
nombre = input("Dígame su nombre: ")
if nombre in personas_autorizadas:
  print("Está autorizado")
else:
  print("No está autorizado")
  

'''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio19.py
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


''''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio21.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: Almacenay y mostrar asiganturas
'''
asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lenguas", "Programacion","Biologia"]
print("Las asiganturas son: ")
for i in range(len(asignaturas)):
  print(i+1,asignaturas[i])

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


''''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio24.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: llenar diccionario vacio 
'''
persona = {}
continuar = True
while continuar:
  clave = input('¿Qué dato quieres introducir? ')
  valor = input(clave + ': ')
  persona[clave] = valor
  print(persona)
  continuar = input('¿Quieres añadir más información (si/no)? ') == "si"


''''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio25.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: Diccionario de traducción español-inglés.
'''
diccionario = {}
palabras = input("***Introduce la lista de palabras y traducciones***"+"\n"+ "Formato= palabra:traducción separadas por comas: "+"\n"+"Ejemplo=Hola: Hi,"+"\n")
for i in palabras.split(','):
  clave, valor = i.split(':')
  diccionario[clave] = valor
frase = input('Introduce una frase en español: ')
for i in frase.split():
  if i in diccionario:
    print(diccionario[i], end=' ')
  else:
    print(i, end=' ')


''''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio26.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: Diccionario con {'Euro':'€', 'Dolar':'US$', 'Peso':’$'} y y monstrar simbolo
'''
divisa = {'Euro':'€', 'Dolar':'US$', 'Peso':'$'}
simbolo = input("Introduzca una divisa: ")
if simbolo.title() in divisa:
    print("Su simbolo es: "+divisa[simbolo.title()])
else:
    print("La divisa no esta en el diccionario.")


''''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio27.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: Preguntar al usuario su nombre, edad, dirección y teléfono y lo guardar en un diccionario y despues mostrar por pantalla
'''
datos={'nombre','edad','direccion','telefono'}
nombre = input('¿Cual es tu nombre? ')
edad = input('¿Cual es tu edad? ')
direccion = input('¿Cual es tu direccion? ')
telefono = input('¿Cual es tu numero de telefono?')
datos = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(" ")
for clave,valor in datos.items(): 
     print ("%s es %s" % (clave, valor))


'''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio28.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: gestionar las facturas pendientes de cobro de una empresa.Se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura.
'''
facturas = {'Facturas':'costo_factura'}
cant_cobrada = 0
cant_pendiente = 0
cuenta = ''
while cuenta != 'S':
    cuenta = input('\n ¿Que deseas hacer? \n Agregar Factura (A) \n Pagar Factura (P)\n Salir (S)? ')
    if cuenta == 'A':
        clave = input('\n¿Cual es el número de la factura? : ')
        costo = float(input('¿Cual es el monto de la factura?: '))
        facturas[clave] = costo
        cant_pendiente += costo
    if cuenta == 'P':
      valido= ''
      while valido != 'X':
        for clave,valor in facturas.items(): 
          print  ('\n',"%s " % (clave),end="")
        clave = input('\n \n Numero de factura a pagar: ')  
        if clave in facturas:       
          costo = facturas.pop(clave,'')
          cant_cobrada += costo
          cant_pendiente -= costo
          valido='X'
        else:
          print("\n ¡¡¡ Esa factura no existe !!!")
          valido = input('\n¿Volver a intentar: Escribe (X) para salir \n')
                  
    print('\nCobrado al momento :', cant_cobrada)
    print('Pendiente de cobrar:', cant_pendiente)


   