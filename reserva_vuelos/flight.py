
"""Este módulo incluye la definición para poder representar vuelos

    Classes:
        Flight
"""

import aircraft 

class Flight:
    """ Representa un vuelo con su avión, pasajeros, asientos libres, etc.

    Args:
        number (int): Numero de vuelo.
        aircraft (Aircraft): Es el avión en el que será el vuelo

    Methods:
        allocate_passenger(): Asigna un asiento a un pasajero
        reallocate_passenger(): Cambia de asiento a un pasajero
        num_available_seats(): Nos dice la cantidad de asientos desocupados
        print_seating(): Imprime en la consola el plano de asientos
        print_boarding_cards(): Imprime en la consola la tarjeta de embarque de cada pasajero
        __parse_seat(): Divide un identificador de asiento en fila y asiento
        __passenger_seats(): Itera la ubicación de los asientos ocupados

    """

    def __init__(self, number, aircraft):
        """Inicializa un vuelo con los datos del mismo

        Args:
            number (int): Número de vuelo
            aircraft (Aircraft): Avión del vuelo

        """
        self.__number = number
        self.__aircraft = aircraft
        self.__seating = []
        filasAsientos, letrasAsientos = self.__aircraft.seating_plan()

        for fila in filasAsientos:
            if(fila != None):
                dic = {}
                for asiento in letrasAsientos:
                    dic[asiento] = None
                
                self.__seating.append(dic)

    
    def allocate_passenger(self, seat, passenger):
        """Asignar un asiento a un pasajero

        Args:
            seat: El asiento como "12C" o "21F
            passenger: Los datos de los pasajeros como ("Jack", "Shephard", "85994003S")

        """
        fila, letra = self.__parse_seat(seat)
        self.__seating[fila][letra] = list(passenger)
    
    def reallocate_passenger(self, from_seat, to_seat):
        """Reasignar un pasajero a otro asiento

        Args:
            from_seat: El asiento actual del pasejero, como "12C
            to_seat: El nuevo asiento de asiento

        """
        filaAntes, letraAntes = self.__parse_seat(from_seat)
        filaNueva, letraNueva = self.__parse_seat(to_seat)
        passenger = self.__seating[filaAntes][letraAntes]
        self.__seating[filaAntes][letraAntes] = None
        self.__seating[filaNueva][letraNueva] = passenger

    
    def num_available_seats(self):
        """Obtiene la cantidad de asientos desocupados

        Returns:
            El número de plazas no ocupadas  

        """
        asientosNoAcupados = 0
        i = 0
        for fila in self.__seating:
            for asiento in fila:
                if self.__seating[i][asiento] == None:
                    asientosNoAcupados += 1
            i += 1
        
        return asientosNoAcupados

    def print_seating(self):
        """Imprime en la consola el plano de asientos

        Ejemplo de una fila:
            {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}

        """
        for fila in self.__seating:
            print(fila)
    
    def print_boarding_cards(self):
        """Imprime en consola la tarjeta de embarque de cada pasajero 

        Ejemplo de una tarjeta de embarque:
            ----------------------------------------------------------
            |     Jack Sheppard 85994003S 15E BA758 Airbus A319      |
            ----------------------------------------------------------
        """
        i = 0
        for fila in self.__seating:
            for passenger in fila:
                info = self.__seating[i][passenger]
                if (info != None):
                    #print(info[0])
                    name = info[0]
                    surname = info[1]
                    id_card = info[2]
                    print( "-----------------------------------------------------------------" )
                    print( "|\t" + name + " " + surname + " " + str(id_card) + " " + str(i) + passenger + " " + str(self.__number) + " " + self.__aircraft.get_model() + "\t\t|")
                    print( "-----------------------------------------------------------------" )
                 
            i += 1


    def __parse_seat(self, seat):
        """ Dividir un identificador de asiento en fila y letra

        Args:
            seat: El identificador del asiento a dividir como "12C
            
        Returns:
            row: La fila del asiento como 12
            letter: La letra del asede, como la "C

        """
        # fila, letra
        return int(seat[:-1]), seat[-1:]
    
    def __passenger_seats():
        """Una función generadora para iterar las ubicaciones de los asientos ocupados

        Returns:
            generator: Tupla de los datos del pasajero y del asiento 
        """