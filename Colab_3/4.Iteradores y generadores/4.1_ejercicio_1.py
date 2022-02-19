
# Escribe una función generadora de la secuencia de Fibonacci y comprueba su correcto funcionamiento. Los valores de esta secuencia se calculan siguiendo la siguiente fórmula:

def fibonacci():
    f0 = 0
    f1 = 1
    

    while True:
        ft = f0 + f1
        yield ft
        f0 = f1
        f1 = ft
        
generador = fibonacci()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))



     
