
"""Este módulo incluye la definición para poder representar vuelos

    Classes:
        Flight
"""

from re import A
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

        if list(filter(lambda l: l.isdigit(), self.__number[:2])) != []:
            raise ValueError("Los primeros dos dígitos del número de vuelo tienen que ser letras")
            
        if list(filter(lambda l: l.islower(), self.__number[:2])) != []:
            raise ValueError("Los primeros dos carácteres del número de vuelo tienen que ser mayúscula")
        
        if list(filter(lambda n: not n.isdigit(), self.__number[2:])) != []:
            raise ValueError("El número de vuelo tiene que llevar números luego de los dos primeros carácteres")

        if int(self.__number[2:]) > 9999:
            raise ValueError("El número es demasiado grande")      

        self.__aircraft = aircraft
        self.__seating = []
        self.__filasAsientos, self.__letrasAsientos = self.__aircraft.seating_plan()

        for fila in self.__filasAsientos:
            if(fila != None):
                dic = {}
                for asiento in self.__letrasAsientos:
                    dic[asiento] = None
                
                self.__seating.append(dic)

    
    def allocate_passenger(self, seat, passenger):
        """Asignar un asiento a un pasajero

        Args:
            seat: El asiento como "12C" o "21F
            passenger: Los datos de los pasajeros como ("Jack", "Shephard", "85994003S")

        """
        fila, letra = self.__parse_seat(seat)
        if self.__seating[fila][letra] != None:
            raise ValueError("El asiento está ocupado")

        self.__seating[fila][letra] = list(passenger)
    
    def reallocate_passenger(self, from_seat, to_seat):
        """Reasignar un pasajero a otro asiento

        Args:
            from_seat: El asiento actual del pasejero, como "12C
            to_seat: El nuevo asiento de asiento

        """
        filaAntes, letraAntes = self.__parse_seat(from_seat)

        if self.__seating[filaAntes][letraAntes] == None:
            raise ValueError("El asiento original está vacío")

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
        


        if list(filter(lambda a: a == seat[-1:], self.__letrasAsientos)) == []:
            raise ValueError("La letra del asiento no existe")

        if list(filter(lambda a: not a.isdigit(), seat[:-1])) != []:
            raise ValueError("El valor de la fíla tiene que ser un número")
       
        if int(seat[:-1]) >= int(self.__filasAsientos[-1]):
            raise ValueError("La fila no existe")

        # fila, letra
        return int(seat[:-1]), seat[-1:]
    
    def __passenger_seats():
        """Una función generadora para iterar las ubicaciones de los asientos ocupados

        Returns:
            generator: Tupla de los datos del pasajero y del asiento 
        """