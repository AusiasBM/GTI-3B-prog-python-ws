

# Crea una función llamada clean_list que tome una lista de nombres de usuarios y una lista de nombres de usuarios baneados y devuelva una nueva lista con los usuarios no baneados.

usuarios = ["Pepe", "alfonso", "ana", "pedro", "juan", "pepito", "Toni"]
usuariosBaneados = ["alfonso", "pedro", "pepito"]


clean_list = filter(lambda user: usuariosBaneados.count(user) <= 0, usuarios)

print(list(clean_list))