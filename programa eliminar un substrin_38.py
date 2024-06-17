print("\n************************")
print("*  programa eliminar un substring  *")
print("************************\n")

string = "Siempre se puede cuando se quiere"
palabra = "cuando se quiere"
print("string: "+string)
print()
print("palabra a quitar: " +palabra)
print()
substring= ""
indice = string.find(palabra)
substring = string[0:indice] + string[indice+len(palabra)+1:len(string)]

print(substring)
