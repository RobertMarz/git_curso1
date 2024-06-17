print("\n************************")
print("*  Programa Bucle for_  *")
print("************************\n")

#__OTRA FORMA_________________________________________________
string = input("Ingrese una frase : ")
letra = input("Ingresa una letra para finalizar : ")

for caracter in string:
    if caracter.lower() == letra.lower():
        break
    elif caracter.lower() == "a":
        continue
    elif caracter.lower() == "e":
        continue
    elif caracter.lower() == "i":
        continue
    elif caracter.lower() == "o":
        continue
    elif caracter.lower() == "u":
        continue
    print(caracter,end="")
