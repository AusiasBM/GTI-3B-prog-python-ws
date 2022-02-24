

class Passenger:

    def __init__( self, name, surname, id_card ):
        self.__name = name
        self.__surname = surname
        self.__id_card = id_card

    def passenger_data(self):
        """ Almacena la información de cada pasajero
        nombre, apellido e id
        Returns: devuelve una tupla con los tres valores
        name: The passenger's name such as 'Jack'
        family_name: The passenger's family name such as 'Shephard'
        id_card: The passenger's id card such as '85994003S'
        """
        return self.__name, self.__surname, self.__id_card