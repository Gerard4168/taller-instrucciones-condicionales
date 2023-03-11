# programa que indique el precio de venta de un articulo

x = int(input("Ingrese el valor del costo del articulo: "))


if x< 3000:
    y = (15*x)/100
    
else:
    if 3000 <= x <= 6000:
        y = 500
    else: 
      y = (25* x)/100


z = x + y 


print(z)