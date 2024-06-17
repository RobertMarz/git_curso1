print(" Recorrer un conjunto con los ciclos for y while_109*")
print("***************************************************************/n")

nums = {1,2,3,4,5}
print()
print(f"conjunto de numeros =  {nums} ")
print("Haciendolo con for")
for ele in nums: # es lo mas adecuado para reccorrer conjunto
    print(ele)


print("Haciendolo con while")
# hay que convertirlo a lista primero
lista_num = list(nums)
longitud = len(lista_num)
i = 0
while i <  longitud:
    print(lista_num[i])
    i +=1

print("fin de ciclo")































