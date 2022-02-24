"""Este módulo incluye la definición para poder representar aviones de tipo: Aircraft, Airbus y Boeing

    Classes:
        Aircraft
        Airbus
        Boeing
"""

# Las clase Aircraft contiene información de la aeronave
class Aircraft:
    """La clase Aircraft contiene información de la aeronave.

    Args:
        resgistration (str): Número de restitro que se le asigna
            model (str): Modelo del avión
            num_rows (int): Número de filas
            num_seats_per_row (int): Número de asientos por fila

    Methods:
        get_registration(): Devuelve el número de registro
        get_model(): Devuelve el modelo
        seating_plan(): Devuelve una tupla con una lista de filas y un str de letras por asiento
        num_seats(): Devuelve el número total de asientos que tiene la aeronave
    """

    def __init__(self, registration, model, num_rows, num_seats_per_row ):
        """Inicializa una aeronave con sus datos

        Args:
            registration (str): Número de restitro que se le asigna
            model (str): Modelo del avión
            num_rows (int): Número de filas
            num_seats_per_row (int): Número de asientos por fila
        """
        self.__registration = registration
        self.__model = model
        self.__num_rows = num_rows
        self.__num_seats_per_row = num_seats_per_row

    def get_registration(self):
        """devuelve el registro

        Returns:
            registration (str): 
        """
        return self.__registration
    
    def get_model(self):
        """Devuelve el modelo de la aeronave

        Returns:
            model (str): Modelo de la aeronave
        """
        return self.__model

    def seating_plan(self):
        """ Devuelve una tupla con dos valores

        Returns:
            rows: Una lista de filas: None, 1, 2, etc.
            seats: Un string de letras como este 'ABCDEF'
        """
        lista = list(range(1, self.__num_rows))
        lista.insert(0, None)
        abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return lista, abecedario[:self.__num_seats_per_row]

    def num_seats(self):
        """Calcula el número total de asientos que tiene la aeronave.
        
        Returns:
            seats: Número de asientos
        """
        return self.__num_rows * self.__num_seats_per_row


class Airbus(Aircraft):
    """La clase Airbus contiene información de la aeronave de este modelo en específico.

    Args:
        resgistration (str): Número de restitro que se le asigna
        variant: Es la variante de aeronave

    Methods:
        get_variant(): Devuelve la variante de la aeronave
        
    """

    def __init__(self, registration, variant):
        """Inicializa una aeronave Airbus con unos datos preasignados

        Args:
            registration (str): Número de restitro que se le asigna
            variant (str): Variante de la aeronave

        """
        super().__init__(registration, "Airbus A319", 23, 6)
        self.__variant = variant

    def get_variant(self):
        """Devuelve la variante de la aeronave

        Returns:
            variant (str): Variante

        """
        return self.__variant

class Boeing(Aircraft):
    """La clase Boeing contiene información de la aeronave de este modelo en específico.

    Args:
        resgistration (str): Número de restitro que se le asigna
        airline: Es la aerolinia de la aeronave

    Methods:
        get_airline(): Devuelve la aerolinia de la aeronave

    """

    def __init__(self, registration, airline):
        """Inicializa una aeronave Boeing con unos datos preasignados

        Args:
            registration (str): Número de restitro que se le asigna
            airline (str): Aerolinea de la aeronave

        """
        super().__init__(registration, "Boeing 777", 56, 9)
        self.__airline = airline

    def get_airline(self):
        """Devuelve la aerolinea de la aeronave

        Returns:
            airline (str): aerolinea
            
        """
        return self.__airline




