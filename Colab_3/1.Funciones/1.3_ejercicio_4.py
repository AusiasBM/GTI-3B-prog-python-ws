

# Crea una función llamada greater_than_average que tome un parámetro x de tipo numérico, y una lista llamada data_array. 
# La función deberá devolver cierto en caso de que el valor x sea mayor que la media de la lista, y falso en caso contrario.

data_array = [1, 2, 3, 4, 5]
x = 4

greater_than_average = lambda list: (sum(list) / len(list)) < x

print(greater_than_average(data_array))