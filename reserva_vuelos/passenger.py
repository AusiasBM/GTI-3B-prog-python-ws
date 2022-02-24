"""Este módulo incluye la definición para poder representar Pasajeros

    Classes:
        Passenger
"""

class Passenger:
    """Representación de un pasajero

    Args:
        name (str): Nombre
        surname (str): Apellidos
        id_card (int): El id de su tarjeta

    """

    def __init__( self, name, surname, id_card ):
        """Inicializa un pasajero con su información

        Args:
            name (str): Nombre
            surname (str): Apellidos
            id_card (int): El id de su tarjeta

        """
        self.__name = name
        self.__surname = surname
        self.__id_card = id_card

    def passenger_data(self):
        """ Devuelve la información de cada pasajero nombre, apellido e id
        
        Returns: ( Es una tupla )
            name: Nombre
            surname: Apellido
            id_card: Id de su tarjeta como este '85994003S'

        """
        return self.__name, self.__surname, self.__id_card