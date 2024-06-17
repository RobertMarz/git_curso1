#Ejemplos simpes de codigo sin validacion-------------
print("==============================")
print(" ASIG_CONCAT_BUSC_EXTRAE_COMP_¡¡! ")
print("============================\n")
#ASIGNAR--------------------------
msg = "Hi there"
msg += " "
msg += "I´m here"
print(msg)
print()

#CONCATENAR------------------------
msg = "ESTO ES: "
msg1 = "CONCA"
msg2 = "TENACION"
print(msg+msg1+msg2)
print()
msg = 10
msg1 = 12
msg2 = msg+msg1
msg2 = str(msg2)
print("LA SUMA ES : "+msg2)
print()

#BUSCAR------------------------------
msg = "ESTO ES UNA PRUEBA"
Texto = "PRUEBA"
print("Cadena Original",msg)
print("Pos de Cadena a Buscar: ",Texto)
Buscar_subca = msg.find(Texto)
print("Posicion de la Subcadena buscada: ",Buscar_subca)
print()
#EXTRAER--------------------------------
msg = "ESTO ES UNA PRUEBA"
Extrae = msg[12:18]
print("Se extrajo: Extrae = msg[12:18] ques es:-> ",Extrae)
print()
#COMPERARAR--------------------------------
msg = "ESTO ES"
msg1 = "CONCA"
msg2 = "ESTO ES"
print(msg==msg1)
print()
print(msg==msg2)
