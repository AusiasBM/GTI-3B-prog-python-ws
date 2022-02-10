

# Crea una función llamada clean_list que tome una lista de nombres de usuarios y una lista de nombres de usuarios baneados y devuelva una nueva lista con los usuarios no baneados.

usuarios = ["Pepe", "alfonso", "ana", "pedro", "juan", "pepito", "Toni"]
usuariosBaneados = ["alfonso", "pedro", "pepito"]

clean_list = [ nombre for nombre in usuarios if usuariosBaneados.count(nombre) <= 0 ]

print(clean_list)
