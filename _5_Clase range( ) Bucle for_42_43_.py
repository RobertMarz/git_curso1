print("\n************************")
print("*  programa de LA CLASE range() y bucle for  *")
print("************************\n")


#__OTRA FORMA_________________________________________________
print("\nGENERAR LA TABLA DE MULTIPLICACION CUALQUIER NUMERO DEL 1-10\n")
NUMERO = int(input("Intoduce Numero a multiplicar : "))
for i in range(0,10):
    #print(i)
    print(NUMERO,"X",i+1,"=",NUMERO*(i+1))
   # print()
print("Fin del for 1.\n")
#__OTRA FORMA_________________________________________________
for i in range(10):
    print(f"{NUMERO} X {i+1} = {NUMERO*(i+1)}")
    #print()
print("Fin del for 2.\n")

print("\n************************")
print("*  LA CLASE range()  *")
print("************************\n")


#__OTRA FORMA_________________________________________________

string = input("Intoduce OTRO string : ")
for i in range(0,len(string)):
    #print(i)
    print(i,string[i],end = "")
print("Fin del for 1.\n")
#__OTRA FORMA_________________________________________________
print("OTRA FORMA DELA CLASE range(0,5): \n")
for i in range(0,5):
    #print(i)
    print(i,end = "")
print("\nFin del for 2.\n")

print("OTRA FORMA DE CLASE range(5,0,-1):  \n")
for J in range(5,0,-1):
    #print(i)
    print(J,end = "")
print("\nFin del for 3.\n")

print("Números impares del 1 al 10")
for i in range(1, 10, 2):
    print(i, end=', ')