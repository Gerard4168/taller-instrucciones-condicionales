# Determinar si un triangulo es obtuso recto o agudo dadas las longitudes de sus 3 lados

Lado_A = int(input("Ingrese el lado Opuesto: "))
Lado_B = int(input("Ingrese el lado Adyacente: "))
Lado_C = int(input("Ingrese ingrese la Hipotenusa: "))

if Lado_A**2 * Lado_B**2 == Lado_C**2:

    print (" Es Recto")

elif Lado_C**2 < Lado_A**2 + Lado_B**2:

    print(" Es Agudo")

elif Lado_C**2 > Lado_A**2 + Lado_B**2:

    print("Es Obtuso")




    