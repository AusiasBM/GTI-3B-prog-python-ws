

"""A parte de ficheros de texto, Python ofrece soporte para leer otros tipos de ficheros, como ficheros binarios (ej. una imagen). 
La manera de leer un fichero binario consiste en abrir el fichero en modo binario (con la opción b). 
Por tanto, la opción rb nos permite abrir el fichero binario para lectura mientras que la opción wb nos permite abrirlo para escritura:"""

f = open('lena.png', 'rb') 
contenido = f.read() 
#print(contenido)

"""Una de las ventajas de Python es la cantidad de paquetes que existen. 
En concreto, el paquete xlwt nos permite trabajar con ficheros Excel. 
A continuación tienes un ejemplo de cómo podemos generar un Excel con diferente información. 
Para profundizar más, puedes consultar la documentación: https://xlwt.readthedocs.io/en/latest/"""

# Hay que instalar la librería con:
# pip3 install xlwt
# ---------------------------------
# import xlwt
# from xlwt import Workbook

# wb = Workbook()

# sheet1 = wb.add_sheet("Sheet 1")

# sheet1.write(1, 0, 'AAAA')
# sheet1.write(2, 0, 'BBBB')
# sheet1.write(3, 0, 'CCCC')
# sheet1.write(4, 0, 'DDDD')
# sheet1.write(5, 0, 'EEEE')
# sheet1.write(0, 1, '1111')
# sheet1.write(0, 2, '2222')
# sheet1.write(0, 3, '3333')
# sheet1.write(0, 4, '4444')
# sheet1.write(0, 5, '5555')

# wb.save("xlwt example.xls")

"""Otro tipo de ficheros que vamos a trabajar son los ficheros separados por comas (CSV). 
A través del paquete csv, podemos leer ficheros de este tipo. 
Observa el siguiente ejemplo cómo podemos leer cada fila y guardarla en una lista:"""
# En ocasiones, un fichero csv utiliza separadores diferentes como un tabulador. 
# Esto lo podríamos especificar también en la llamada a reader:

import csv
with open('california_housing_test.csv', 'r') as file:
    reader = csv.reader(file)  # reader = csv.reader(file, delimiter = "\t")
    for row in reader:
        print(row)

# Si quieres profundizar más, puedes acceder a la documentación: https://docs.python.org/3/library/csv.html