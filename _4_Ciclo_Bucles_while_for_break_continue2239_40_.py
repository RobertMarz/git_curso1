print("\n************************")
print("* BUCLES O CICLOS BREAK Y CONTINUE *")
print("************************\n")

 #Ejemplo 1
print('Ejemplo sencillo de while')
x =1
while x < 3:
    print(x)
    x+=1
    

#Ejemplo 2 while con else
print('Ejemplo sencillo de while con else')
count = 0
while(count < 2):
    count = count+1
    print("Iteración número {}".format(count))
else:
    print("Bucle while con else finalizado")

  #Ejemplo 3
x =1
while x < 5:
    print("Breake",x)
    x+=1
    if x == 3:
        break #breake rompe el ciclo salta en 3

print('ejemplo while con continue') 

  #Ejemplo 4
x =1
while x < 5:
    x+=1
    if x == 3:
        continue
    print("continue",x) #continue permite seguir el while sin hacer este
   

  
print("\n************************")
print("*  Uso del ciclo o bucle for  *")
print("************************\n")

string = input("Intoduce un string : ")
for character in string:
    print(character)
print("Fin del for 1.")

#__OTRA FORMA_________________________________________________

string = input("Intoduce OTRO string : ")

for i in range(0,len(string)):
    #print(i)
    print(i,string[i],end = "")
print("Fin del for 2.\n")

string = input("Intoduce OTRO string : ")
string_rev = ""
for Car in string:
    string_rev = Car + string_rev 
    print(string_rev)
print("Fin del for 3.\n")

alumnos = ["Ane", "Mikel", "Unai", "Lorea"]
for alumno in alumnos:
    print(alumno)
else:
    print("no quedan mas alumnos")