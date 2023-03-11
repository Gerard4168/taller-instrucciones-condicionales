# Programa que lea dos números enteros y averigüe si el uno es múltiplo del otro

a=int(input("ingrese el primer valor: "))
b=int(input("ingrese el segundo valor: "))


c= a%b
if c == 0:
    d=b%a
    if d == 0:
        rta= f"{a} es igual a {b}"
    else:
        rta=f"{a} es multiplo de {b}"
else:
    d=b%a
    if d == 0:
        rta = f"{b} es multiplo de {a}"
    else:
        rta=f"{a} y {b} no son multiplos"

        print(rta)