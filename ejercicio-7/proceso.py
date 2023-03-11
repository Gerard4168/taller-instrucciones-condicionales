# Programa para determinar si dados tres números enteros, la suma de los dos primeros es igual al tercero

A = int(input("ingrese el valor de a: "))
B = int(input("ingrese el valor de b: "))
C = int(input("ingrese el valor de c: "))

D = A+B


if D==C :
    rta = ("La suma de a y b son iguales que C")
else: 
    rta = ("La suma de a y b no son iguales que C")

    print(rta)