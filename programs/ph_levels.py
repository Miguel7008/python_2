ph = int(input('del 0 al 14 elige un numero para determinar el ph: '))

if  ph > 7:
    print('Basico')
elif ph < 7:
    print('Acido')
else:
    print('Neutro')