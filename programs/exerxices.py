#Calculadora
'''
numero = int(input('Digite el numero de las tablas del 1 al 10: '))
for  x in range(1,11):
     
     if numero <=10:
         result=(numero*x)
         print(numero,'*',x, '=',result)
'''
'''#numeros pares hasta 100

par = 0
suma = 0
while par <= 100:
    print(par)
    par += 2
    #suma = suma + par
    suma += par
print('La suma de los numeros pares es: ',suma)
'''
'''
for hora in range (24):
    for x in range(0,60):
        for y in range(0,60):
         print(hora,':',x,':',y)
         if hora == 23 and x == 59 and y == 59:
            break
'''




contador = 0
peso_niños = 0
peso_jóvenes = 0
peso_adultos = 0
peso_viejos = 0
cantidad_niños = 0
cantidad_jóvenes = 0
cantidad_adultos = 0
cantidad_viejos = 0

while contador < 5:
    edad = int(input("Ingrese la edad de la persona: "))
    peso = float(input("Ingrese el peso de la persona: "))

    if edad <= 5:
        peso_niños += peso
        cantidad_niños += 1
    elif edad >= 13 and edad <= 29:
        peso_jóvenes += peso
        cantidad_jóvenes += 1
    elif edad >= 30 and edad <= 49:
        peso_adultos += peso
        cantidad_adultos += 1
    elif edad > 60 :
        peso_viejos += peso
        cantidad_viejos += 1
        

    contador += 1

promedio_niños = peso_niños / cantidad_niños if cantidad_niños != 0 else 0
promedio_jóvenes = peso_jóvenes / cantidad_jóvenes if cantidad_jóvenes != 0 else 0
promedio_adultos = peso_adultos / cantidad_adultos if cantidad_adultos != 0 else 0
promedio_viejos = peso_viejos / cantidad_viejos if cantidad_viejos != 0 else 0

print("Promedio de peso de niños:", promedio_niños)
print("Promedio de peso de jóvenes:", promedio_jóvenes)
print("Promedio de peso de adultos:", promedio_adultos)
print("Promedio de peso de viejos:", promedio_viejos)
        




         

      




        


         




        



       


    

         
