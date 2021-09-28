def array_sumador(array):
    suma = 0
    for i in range(len(array)):
        suma = suma + array[i]
    return suma

print("La suma de los numeros ingresados es: ",array_sumador(array))