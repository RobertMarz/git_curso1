print(" Proyecto #4  Conversor de romano a entero entre 1 y 3999  /n")
try:
    Valores_Romanos = {"I":1,
                       "V":5,
                       "X":10,
                       "L":50,
                       "C":100,
                       "D":500,
                       "M":1000}
    
    num = input("ingrese un romano para convertirlo a Entero: ")
    num = num.upper()

    num_entero = 0
    valor_anterior = 0
    for caracter in num[::-1]: #[inicio:stop:step] superstring
        valor_Actual = Valores_Romanos.get(caracter,0) # el get valida que este sino retorna o
        
        if valor_Actual < valor_anterior:
            num_entero -= valor_Actual
        else:
            num_entero += valor_Actual

        valor_anterior = valor_Actual

    print("Resultado: ",num_entero)

except Exception as e:
    print("Valor No valido",e)
