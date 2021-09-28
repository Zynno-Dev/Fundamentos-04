def multiplicar(a,b):
    c = a
    for i in range(b-1):
        a+=a
    return a-c

print(multiplicar(6,3))