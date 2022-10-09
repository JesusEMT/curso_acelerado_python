''''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion3/ejercicio28.py
Autor: Programador Jesus Emmanuel Martinez Torres
Action: gestionar las facturas pendientes de cobro de una empresa.Se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura.
'''
facturas = {}
cant_cobrada = 0
cant_pendiente = 0
cuenta = ''
print("\n -------------------------------")
print(" | ¡¡      BIENVENIDO !!        |")
print(" -------------------------------")
while cuenta != '3':
    cuenta = input('\n ¿Que deseas hacer? \n 1. Agregar Factura. \n 2. Pagar facturas. \n 3. Salir del sistema. :')
    if cuenta == '1':
          clave = input('\n¿Cual es el número de la factura? : ')
          if clave not  in facturas:  
            costo = float(input('¿Cual es el monto de la factura?: '))
            facturas[clave] = costo
            cant_pendiente += costo
            print("\n -------------------------------")
            print(" |  Factura ",clave," Agregada     |")
            print(" -------------------------------")
          else:
            print("\n -------------------------------")
            print(" | ¡¡ Esa factura ya existe !! |")
            print(" -------------------------------")
    if cuenta == '2':
      if facturas:
        valido= ''
        while valido != 'S':
          print("---------------------------")
          print("| No. Factura |  Monto    |")
          print("---------------------------")
          for clave,valor in facturas.items():         
            print (clave,end="  $")
            print (valor)
          print("---------------------------")  
          clave = input('\n \n Numero de factura a pagar: ')  
          if clave in facturas:       
            costo = facturas.pop(clave,'')
            cant_cobrada += costo
            cant_pendiente -= costo
            print("\n -------------------------------")
            print(" |      Facturada con exito     |")
            print(" -------------------------------")
            valido='S'
          else:
            print("\n -------------------------------")
            print(" | ¡¡ Esa factura no existe !! |")
            print(" -------------------------------")
            valido = 'S'
      else:
        print("\n -------------------------------")
        print(" | NO hay facturas registradas |")
        print(" -------------------------------")        
    print('\nCobrado al momento : $', cant_cobrada)
    print('Pendiente de cobrar: $', cant_pendiente)
    print('---------------------------------------')
print("\n -------------------------------")
print(" | ¡¡      HASTA LUEGO !!       |")
print(" -------------------------------")



   
