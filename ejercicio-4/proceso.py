# programa que calcule el índice de masa corporal

x = int(input("ingrese el valor del peso en kg: "))
y = float(input("ingrese el valor de la altura en m: "))


z = x/(y**2)


if z<16:
    rta= "Criterio de ingreso al hospital"
else:
    if 16<=z<17:
        rta = "infra-peso"
    else:
        if 17<=z<18:
            rta= "Peso-bajo"
        else:
            if 18<=z<25:
                rta="peso normal-saludable)"
            else:
                if 25<=z<30:
                    rta= "Sobrepeso-obesidad grado I)"
                else:
                    if 30<=z<35:
                        rta= "Sobrepeso cronico-obesidad grado II)"
                    else:
                        if 35<=z<40:
                            rta="Obesidad premorbida-obesidad grado III)"
                        else:
                            rta= "Obesidad morbida-obesidad de grado IV)"
print(rta)