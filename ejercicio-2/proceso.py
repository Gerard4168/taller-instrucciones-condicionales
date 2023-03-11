# Programa para aprovar creditos

x = int(input("Ingrese el valor de su sueldo actual: "))

if x<945200 :

    rta = "Tu credito fue denegado"

else :

    y = int(input("si tiene deudas ingrese el número 1, si no ingrese cualquier otro numero: "))

    if y==1 :
        
        rta= "Su credito fue denegado"

    else : 

        rta = "Su credito fue aprovado"

print (rta)