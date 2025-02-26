def es_par_o_impar(num):
    if num % 2 ==0:
        return "par"
    else:
        return "impar"
numero= int (input("introduce un numero: "))
print (f"el numero {numero} es {es_par_o_impar (numero)}")