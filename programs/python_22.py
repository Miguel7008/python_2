'''#Numero positivo, negativo y neutro

Numero = int(input('Ingrese un numero: '))
if Numero > 0:
    print('El numero',Numero, 'es positivo')
elif Numero < 0:
    print('El numero',Numero, 'es negativo')
elif Numero == 0:
    print('El numero',Numero, 'es neutro')
'''
#Lapices
'''
Lapiz = float(input('Ingrese la cantidad de lapices a comprar: '))
if Lapiz >= 1000:
    Total = Lapiz * 150
    print('El total a pagar es de:',Total)
else:
    Total_2 = Lapiz * 250
    print('El total a pagar es de:',Total_2)
'''
'''#Producto, clave y descuento

Producto = input('Digite el nombre del producto: ')
Clave = int(input('Clave del producto: '))
precio = float(input('Digite el precio del producto: '))
if Clave == 1:
    Des_1 = precio * 0.1
    Total = precio - Des_1
    print('El total a pagar es de:',Total)
elif Clave == 2:
    Des_2 = precio * 0.2
    Total_2 = precio - Des_2

    print('El total a pagar es de:',Total_2)
else:
 print('precio:',precio)

print('producto:',Producto, '----------------------')
print('clave:',Clave,'-----------------------------')
print('precio original:',precio,'------------------')
print('total a pagar:',Total,'---------------------')
'''

'''# asignaturas


asignatura = float(input('Digite la nota de Matemáticas: '))
asignatura_2 = float(input('Digite la nota de Español: '))
asignaturas_3 = float(input('Digite la nota de Ingles: '))
asignaturas_4 = float(input('Digite la nota de Ed. Fisica: '))
asignaturas_5= float(input('Digite la nota de Filosofía: '))
asignaturas_6 = float(input('Digite la nota de Física : '))
asignaturas_7 = float(input('Digite la nota de Tecnología: '))
asignaturas_8 = float(input('Digite la nota de Inoformatica: '))
asignaturas_9 = float(input('Digite la nota de Religión: '))
asignaturas_10 = float(input('Digite la nota de química: '))

matricula = 3500000
suma = asignatura + asignatura_2 + asignaturas_3 + asignaturas_4 + asignaturas_5 + asignaturas_6 + asignaturas_7 + asignaturas_8 + asignaturas_9 + asignaturas_10
promedio = suma / 10 

if promedio >= 4.5:
    descuento = matricula * 0.3
    total = matricula - descuento
    print('El total a pagar con descuento es:',total)
   
   
else:
    iva = matricula * 0.1
    total_2 = matricula + iva
    print('La matricula a pagar con iva es:',total_2)
   
'''


#rifas

Cuenta = float(input('Digite el valor de la cuenta: '))
Balota = int(input('digite el numero de la boleta: '))

if Balota == 1:
    print('gana una bolsa de leche')
    print('El valor de la cuenta es:',Cuenta)
elif  Balota == 2:
    print('Gana una libra de arroz')
    print('El valor de la cuenta es:',Cuenta)
elif Balota == 3:
    print('No gana')
    print('El valor de la cuenta es:',Cuenta)
elif Balota == 4:
    print ('Gana descuento del 15%')
    descuento = Cuenta * 0.15
    total = Cuenta - descuento
    print('El valor de la cuenta es de:',total)
elif Balota == 5:
    print('Intente de nuevo')
elif Balota == 6:
    print('Gana descuento del 10%')
    descuento_2 = Cuenta * 0.1
    total_2 = Cuenta - descuento_2
    print('El valor de la cuenta es de:',total_2)
elif  Balota == 7:
    print('Gana un paquete de papas fritas')
    print('El valor de la cuenta es de:',Cuenta)
elif Balota == 8:
    print(' gana un descuento del 12%')
    descuento_3 = Cuenta * 0.12
    total_3 = Cuenta - descuento_3 
    print('El valor de la cuenta es de:',total_3)
elif Balota == 9:
    print('gana un dulce')
    print('El total a pagar es:',Cuenta)
else:
    print('Numero no valido')
    


