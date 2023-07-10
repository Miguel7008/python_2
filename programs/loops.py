#Numeros del 1 al 100
'''
contador = 1
while contador <= 100:
    print(contador)
    contador += 1
print('fin')    
'''
#la suma de cinco numeros
'''
contador= 1
suma = 0
while (contador <= 5):
    suma+= contador
    print(contador)
    contador+= 1
print('La suma de los primeros cinco numeros es de:',suma)
'''
#Numeros menores que 100
'''
Numero = int(input('Digite un numero '))

while Numero > 100:
    print('El numero',Numero, 'es mayor que 100')
else:
    print('El numero',Numero,'es menor que 100')
   '''
    

"""
suma=0
contador = 1
for x in range(10):
    numero = int(input('Digite el numero: '))
    if numero > 0 :
        x = x + 1
    print('Has introducido',x,'numeros positivos mayores que cero')
    print('La suma de los numeros positivos es de: ',suma)
"""
#aprobados

zero = 0
ten = 0
Reprobados = 0
Aprobados = 0
for nota_1 in range(1,35):
    nota_1= int(input('Digite la nota '))
    if nota_1 >= 5:
     # Aprobados = Aprobados + 1
     Aprobados += 1

    if nota_1 < 5:
           # Reprobados = Reprobados + 1
           Reprobados += 1
            
    if nota_1 == 10:
         ten = ten + 1
         
    if nota_1 == 0:
         zero = zero + 1
         
print('El numero de aprobados es de: ',(Aprobados / 35) *100 )
print('El numero de reprobados es de: ',(Reprobados / 35)*100)
print('El numero de estudiantes con diez es de: ',ten)
print('El numero de estudiantes con ceros es de: ',zero)
'''         

       
        


#Contraseña
'''
intentos = 0
digito = ''

while intentos < 3 :
    digito = input('Digite la contraseña: ')
    if digito =="352" or digito == "259" or digito == "569":
       print('Contraseña valida')
       break
    else:
        intentos += 1  
if intentos==3:
    print('Demasiados intentos')
'''
#Numeros positivos 

contador = 0

for x in range(10):
    numero = int(input('Digite el número: '))
    if numero > 0:
        contador += 1
print('Has introducido', contador, 'números positivos mayores que cero')

# cantidad de numeros positivos y  negativo y la suma
'''
suma = 0
contador = 0

while contador < 5 :
    numero = int(input('digite un numero: '))
    contador += 1
    suma = suma + numero
    if numero < 0:
        print('el numero es negativo')
print('Has introducido',contador,'positivos')
print('La suma de los numeros es de: ',suma)
'''
'''#vacunas

Existencias = 1000
 
while Existencias >=200:
    entrega = int(input('digite la cantidad de vacunas: '))
    Existencias = Existencias - entrega
else:
 print('El inventario ha disminuido de 200 vacunas a',Existencias, 'porfavor comuniquelo' )
'''
#viveres
'''
precio = 0
precio_n = 0


x = 1
while x < 6:
    precio = float(input('Digite el precio actual: '))
    valor_inf = float(input('Digite la inflación del mes: '))
    precio = (precio * valor_inf) + precio
    x += 1
    print('El nuevo precio es de: ',precio)
else:
    print('Error')

'''
#fecha del mes

Ndia = int(input('Introduzca el numero del día: '))
Nmes = int(input('Digite el mes: '))
if Ndia >= 1 and Ndia <= 31 and Nmes >=1 and Nmes<=12:
    match Nmes:
        case 1:
            NDia = Ndia 
        case 2:
            NDia = Ndia + 31
        case 3:
            NDia = Ndia + 59
        case 4:
            NDia = Ndia + 90
        case  5:
            NDia = Ndia + 120
        case 6:
            NDia = Ndia + 151
        case 7:
            NDia = Ndia + 181
        case 8:
            NDia = Ndia + 212
        case 9:
            NDia = Ndia + 243
        case 10:
            NDia = Ndia + 273
        case 11:
            NDia = Ndia + 304
        case 12:
            NDia = Ndia + 334
    print('el numero del dia',Ndia, 'del mes',Nmes,'del' ,NDia, 'año: ')
else:
 print ('Datos no validos')
'''
