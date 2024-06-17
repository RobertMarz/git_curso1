print("\n************************")
print("*  PROGRAMA DE LISTAS *")
print("************************\n")

lista = ["A","B","b","c","E","E","f"]
print(f"\n Lista Original {lista}")
ele = input("Ingrese elemento a eliminar de la lista : ")
# puede ser for caracter in lista:
# hace solo la iteracion no almacena en memoria for _ in lista:
for _ in lista:
    if ele.lower() in lista:
        lista.remove(ele.lower())
    elif ele.upper() in lista:
        lista.remove(ele.upper())
    else:
        print(f"\n el elemento: {ele} no esta en la Lista: {lista}")
        break
print(f"\n Lista sin el elemento eliminado: {lista}")
    

