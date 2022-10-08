''''
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


   
