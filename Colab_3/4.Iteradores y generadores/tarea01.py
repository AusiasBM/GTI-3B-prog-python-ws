
# Escribe un programa llamado tarea01.py que permita gestionar clientes mediante un diccionario. Cada cliente estará definido según puedes ver en la siguiente imagen (no cambies los nombres):

# ---------------- VARIABLES ----------------

from xmlrpc.client import boolean


cliente1 = {
    "NIF": "45868877F",
    "name": "Pepe",
    "address": "Calle facundo, 23",
    "phone": "654456789",
    "email": "test1@test.com",
    "VIP": False
}

cliente2 = {
    "NIF": "45868834X",
    "name": "Pepa",
    "address": "Calle facundo, 232",
    "phone": "654456798",
    "email": "test2@test.com",
    "VIP": True
}

dicClientes = {
    "45868877F": cliente1,
    "45868834X": cliente2
}

# ---------------- FUNCIONES ----------------

def add_client(nif, name, address, phone, email, vip):
    """ se preguntarán los datos del cliente y se añadirán al diccionario.
    Args: nif (string), name (string), address (string), phone (string), email (string), vip (bool)
    """

    dicClientes[nif] = {
        "NIF": nif,
        "name": name,
        "address": address,
        "phone": phone,
        "email": email,
        "VIP": vip
    }


def delete_client(nif):
    """ se preguntará su NIF y se borrará el cliente.
    Args: nif (string)
    """
    del dicClientes[nif]


def get_client(nif):
    """ se preguntará su NIF y se mostrarán sus datos.
    Args: nif (string)
    Returns: nif (string), name (string), address (string), phone (string), email (string), vip (bool)
    """

    cliente = dicClientes.get(nif)

    return cliente["NIF"], cliente["name"], cliente["address"], cliente["phone"], cliente["email"], cliente["VIP"]


def get_clients():
    """ se mostrarán los datos de todos los clientes.
    Returns: iterator
    """
    return iter(dicClientes.values())

def get_vip_clients():
    """ se mostrará los datos de todos los clientes que sean VIP.
    Returns: dictionary
    """ 
    dicReturn = {}
    clients = [dicClientes.get(c) for c in dicClientes if dicClientes.get(c)["VIP"]]
    
    for i in clients:
        dicReturn[i['NIF']] = i
    
    return dicReturn

# ---------------- MAIN ----------------

def menu():
    print("MENÚ ---------------------- " )
    print("1. Añadir cliente" )
    print("2. Borrar cliente")
    print("3. Mostrar cliente")
    print("4. Listar clientes")
    print("5. Listar clientes VIP")
    print("6. Terminar")

    print("--------------------------- " )

# -------------- MAIN --------------

salir = False



while salir != True:
    menu()
    opcion = int( input("Dime el número de la opción que deseas: ") )

    print()
    print("--------------------------------------------------------------------------------")

    if opcion == 1: # Añadir cliente

        nif = str(input("NIF: "))
        name = str(input("name: "))
        address = str(input("address: "))
        phone = str(input("phone: "))
        email = str(input("email: "))
        vip = boolean(input("VIP ( True or False ): "))

        add_client(nif, name, address, phone, email, vip)

    elif opcion == 2: # Borrar cliente

        nif = str(input("Dime el NIF del usuario: "))
        delete_client(nif)

    elif opcion == 3:

        nif = str(input("Dime el NIF del usuario: "))
        tupla = get_client(nif)
        
        print(tupla)

    elif opcion == 4: # Listar clientes
        iterador = get_clients()
        i = 0
        while i < len(dicClientes): 
            print(next(iterador))
            i += 1
        
    elif opcion == 5: # Listar clientes VIP
        dicVip = get_vip_clients()

        for c in dicVip:
            print(dicVip.get(c))

    elif opcion == 6:
        salir = True
    else:
        print("Esa opción no existe!!!")

    print("--------------------------------------------------------------------------------")
    print()





