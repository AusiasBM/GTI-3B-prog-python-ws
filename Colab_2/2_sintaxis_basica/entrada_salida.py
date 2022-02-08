
print("Mensaje sin variable")

x = 5

#Dos formas diferentes de hacer el print en Python 3
print("El valor es " + str(x)) #un int no puede imprimirse si no lo convertimos a string previamente
print("El valor es ", x)

x = 5

print("El valor es {0} y si queremos otro valor sería así {1}".format(x, x/3)) #dentro de format ponemos los valores en orden que queremos imprimir
print("El valor es {1} y si queremos otro valor sería así {0}".format(x, x/3)) #podemos cambiar el orden
print("El valor es {0} y si queremos otro valor sería así {a}".format(x, a=x/3)) #... y utilizar variables
print("El valor es {0:.3f} y si queremos otro valor sería así {a:.2f}".format(x, a=x/3)) #... y si queremos formatear los decimales de la salida

#Si queremos en Python 2
#print "Esto sería sin paréntesis"

a = int(input("Introduce el radio:")) #a es de tipo int

b = float(input("Introduce el radio:")) #b es de tipo float

a = b #a cambia a float

a = "Ahora pasa a ser una cadena" #a cambia a cadena

#Mira este ejemplo donde combinamos entrada con varias maneras de mostrar la salida
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

sum = num1 + num2

print("El resultado de sumar ",num1," y ",num2," es ",sum)
print("El resultado de sumar {0} y {1} es {2}".format(num1, num2, sum))
print("El resultado de sumar "+str(num1)+" y "+str(num2))