array = []
def crear_array(min,max):
    c = int(input("Ingrese un numero: "))
    while not((c>=min and c<=max) or c ==-1):
        print("El numero ingresado no es valido")
        c = int(input("vuelva a ingresar un numero: "))

    if c==-1:
        print("Ningun numero ingresado en el array. -Saliendo de la funcion-")

    while not(c==-1):
            array.append(c)
            c = int(input("Ingrese un numero: "))
            while not((c>=min and c<=max) or c ==-1):
                print("El numero ingresado no es valido")
                c = int(input("vuelva a ingresar un numero: "))

    return array

min = int(input("Ingrese el numero minimo: "))
max = int(input("Ingrese el numero maximo: "))

while (min>=max):
    print("Los margenes no son validos.")
    min = int(input("Ingrese el numero minimo: "))
    max = int(input("Ingrese el numero maximo: "))

crear_array(min,max)
print(array)