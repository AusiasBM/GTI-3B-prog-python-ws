
import aircraft 

class Flight:

    def __init__(self, number, aircraft):
        self.__number = number
        self.__aircraft = aircraft
        self.__seating = []
        filasAsientos, letraAsientos = self.__aircraft.seating_plan()
        for fila in filasAsientos:
            if(fila != None):
                #print(fila)
                dic = {}
                for asiento in letraAsientos:
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
        passenger = self.__seating[from_seat[:-1]][from_seat[-1:]].pop()
        self.__seating[to_seat[:-1]][to_seat[-1:]] = passenger

    
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
        Examen de una tarjeta de embarque:
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