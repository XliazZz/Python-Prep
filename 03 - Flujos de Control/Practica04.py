#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

a = 3

if (a < 0):
    print('El número', str(a), 'es menor a cero')
elif (a > 0):
    print('El número', str(a), 'es mayor a cero.')
else:
    print('El número es igual a cero')


#2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

b = True
c = 1

if (type(b) == type(c)):
    print('Los caracteres son del mismo tipo de dato.')
else:
    print('Los caracterces son de diferentes tipos de dato.')


#3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

for i in range(1, 21):
    if i % 2 == 0:
        print('El número', str(i), 'es par')
    else:
        print('El número', str(i), 'es impar')


#4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

for i in range(0,6):
    print('El valor de', str(i), 'elevado a la tercera potencia es:', str(i**3))


#5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

d = 5

for i in range(0,d):
     print(i)


#6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

n = 5
factorial = 1
if (type(n) == int):
    if (n > 0):
        n_original = n
        while (n > 1):
            factorial = factorial * n
            n -= 1
        print('El factorial de', n_original, 'es', factorial)
    else:
        print('La variable debe ser mayor a cero.')
else:
    print('La variable tiene que ser un número entero.')


#7) Crear un ciclo for dentro de un ciclo while

n = 1
while (n < 4):
    n += 1
    for i in range (0, n):
        print('Ciclo while nro: ', str(n))
        print('Ciclo for nro: ', str(i))


###
var = 'elias'
print(var)
###


#8) Crear un ciclo while dentro de un ciclo for

n = 5
for i in range(1, n):
    while(n < 5):
        n -= 1
    print('Ciclo while nro ', str(n))
    print('Ciclo for nro ', str(i))


#9) Imprimir los números primos existentes entre 0 y 30

for num in range(0, 31):
    primo = True
    for i in range(2, num):
        if (num % i == 0):
            primo = False
    if (primo):
        print(num, 'es primo')


#10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

for num in range(0, 31):
    primo = True
    for i in range(2, num):
        if (num % i == 0):
            primo = False
            break
    if (primo):
        print(num, 'es primo')

###
var = 'elias'
print(var)
###

#11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

ciclos_sin_break = 0

for num in range(0, 31):
    primo = True
    for i in range(2, num):
        if (num % i == 0):
            primo = False
            ciclos_sin_break += 1
    if (primo):
        print(num, 'es primo')
print('Cantidad de ciclos:', str(ciclos_sin_break))

###
var = 'elias'
print(var)
###

ciclos_con_break = 0

for num in range(0, 31):
    primo = True
    for i in range(2, num):
        if (num % i == 0):
            primo = False
            ciclos_con_break += 1
            break
    if (primo):
        print(num, 'es primo')
print('Cantidad de ciclos con break:', str(ciclos_con_break))
print('Se optimizó a un', str(ciclos_con_break/ciclos_sin_break), '% de ciclos aplicando break')


###
var = 'elias'
print(var)
###



#12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

ciclos_sin_break = 0

for num in range(0, 101):
    primo = True
    for i in range(2, num):
        if (num % i == 0):
            primo = False
            ciclos_sin_break += 1
    if (primo):
        print(num, 'es primo')
print('Cantidad de ciclos sin break:', str(ciclos_sin_break))

###
var = 'elias'
print(var)
###

ciclos_con_break = 0
for num in range(0, 101):
    primo = True
    for i in range(2, num):
        if (num % i == 0):
            primo = False
            ciclos_con_break += 1
            break
    if (primo):
        print(num, 'es primo')
print('Cantidad de ciclos con break:', str(ciclos_con_break))
print('Se otimizó un', str(ciclos_con_break/ciclos_sin_break), '% utilizando break')


## 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

n = 100

while (n <= 300):
    n += 1
    if ( n % 12 !=0):
        continue
    print(str(n), 'es divisible por 12')


## 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

for num in range(0, 100):
    primo = True
    for i in range(2, num):
        if (num % i == 0):
            primo = False
            break
    if (primo):
        print(num, 'es primo')
        print('¿Desea encontrar otro número primo?')
        if (input() !=num):
            print('Proceso finalizado')
            break


## 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

n = 100
while (n <= 300):
    if (n % 6 == 0):
        print('El número es:', str(n))
        break
    n += 1


