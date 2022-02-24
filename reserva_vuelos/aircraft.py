
# Las clase Aircraft contiene información de la aeronave
class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row ):
        self.__registration = registration
        self.__model = model
        self.__num_rows = num_rows
        self.__num_seats_per_row = num_seats_per_row

    def get_registration(self):
        return self.__registration
    
    def get_model(self):
        return self.__model

    def seating_plan(self):
        """ Genera una tupla con dos valores
        El primero: una lista de los números de filas, siendo none el primer elemento de la lista.
        El segundo: Un string de letras ( ej. 'ABCDEF' )
        Esta tupla nos dice las filas que hay y los asientos por filas
        Returns:
        rows: A list of rows: None, 1, 2, etc.
        seats: A string of letters such as 'ABCDEF'
        """
        lista = list(range(1, self.__num_rows))
        lista.insert(0, None)
        abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return lista, abecedario[:self.__num_seats_per_row]

    def num_seats(self):
        """Calcula el número total de asientos que tiene la aeronave.
        Returns:
        seats: The number of seats
        """
        return self.__num_rows * self.__num_seats_per_row


class Airbus(Aircraft):

    def __init__(self, registration, variant):
        super().__init__(registration, "Airbus A319", 23, 6)
        self.__variant = variant

    def get_variant(self):
        return self.__variant

class Boeing(Aircraft):

    def __init__(self, registration, airline):
        super().__init__(registration, "Boeing 777", 56, 9)
        self.__airline = airline

    def get_airline(self):
        return self.__airline




