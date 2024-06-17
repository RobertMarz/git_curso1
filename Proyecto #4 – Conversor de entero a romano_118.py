print(" Proyecto #4  convertir entero a Romano entre 1 y 3999  /n")
try:
    num = int(input("ingrese un numero entero para convertirlo a Romano: "))
    if 0 < num < 4000:
        print("el numero ingresado debe estar entre 1 y 3999")
        M = ["","M","MM","MMM"] # del 1000 al 3000 en Rom
        C = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"] # del 100 al 900 en Rom
        D = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"] # del 10 al 90 en Rom
        U = ["","I","II","III","IV","V","VI","VII","VIII","IX"] # del 1 al 9 en Rom
        # una division entera para obtener el primer digito

        print(f"{M[num//1000]}{C[(num % 1000)//100]}{D[(num % 100)//10]}{U[(num % 10)]}")

    else:
        print("el numero ingresado debe estar entre 1 y 3999")

except ValueError:
    print("Debe ingresar un ENTERO")
except Exception as e:
    print("Valor No valido",e)
