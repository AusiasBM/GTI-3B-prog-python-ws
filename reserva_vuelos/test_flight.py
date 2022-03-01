

import pytest
import flight
from aircraft import *
from passenger import Passenger


# Creación de objetos flight
def test_exception_message_primeros_digitos():
    with pytest.raises(ValueError) as err:
        flight.Flight(number = "1A117", aircraft = Aircraft(registration = "G-EUAH", model = "Airbus A319", num_rows = 22, num_seats_per_row=6))
    assert "Los primeros dos dígitos del número de vuelo tienen que ser letras" == str(err.value)

def test_exception_message_mayuscula():
    with pytest.raises(ValueError) as err:
        flight.Flight(number = "bA117", aircraft = Aircraft(registration = "G-EUAH", model = "Airbus A319", num_rows = 22, num_seats_per_row=6))
    assert "Los primeros dos carácteres del número de vuelo tienen que ser mayúscula" == str(err.value)


def test_exception_message_numeros_luego():
    with pytest.raises(ValueError) as err:
        flight.Flight(number = "BA11a", aircraft = Aircraft(registration = "G-EUAH", model = "Airbus A319", num_rows = 22, num_seats_per_row=6))
    assert "El número de vuelo tiene que llevar números luego de los dos primeros carácteres" == str(err.value)

def test_exception_message_numero_grande():
    with pytest.raises(ValueError) as err:
        flight.Flight(number = "BA11111", aircraft = Aircraft(registration = "G-EUAH", model = "Airbus A319", num_rows = 22, num_seats_per_row=6))
    assert "El número es demasiado grande" == str(err.value)

def test_return_flight():
    assert type(flight.Flight(number = "BA117", aircraft = Aircraft(registration = "G-EUAH", model = "Airbus A319", num_rows = 22, num_seats_per_row=6))) == flight.Flight

def test_allocate_passenger_exception_message():
    with pytest.raises(ValueError) as err:
        vuelo = flight.Flight(number = "BA117", aircraft = Aircraft(registration = "G-EUAH", model = "Airbus A319", num_rows = 22, num_seats_per_row=6))
        p1 = Passenger("Jack", "Shephard", "85994003S")
        p2 = Passenger("Kate", "Austen", "12589756P")
        vuelo.allocate_passenger("12A", p1.passenger_data())
        vuelo.allocate_passenger("12A", p2.passenger_data())
    assert "El asiento está ocupado" == str(err.value)

def test_reallocate_passenger_exception_message():
    with pytest.raises(ValueError) as err:
        vuelo = flight.Flight(number = "BA117", aircraft = Aircraft(registration = "G-EUAH", model = "Airbus A319", num_rows = 22, num_seats_per_row=6))
        p1 = Passenger("Jack", "Shephard", "85994003S")
        vuelo.allocate_passenger("12A", p1.passenger_data())
        vuelo.reallocate_passenger("12B", "1A")
    assert "El asiento original está vacío" == str(err.value)

def test_num_available_seats():
     vuelo = flight.Flight(number = "BA117", aircraft = Aircraft(registration = "G-EUAH", model = "Airbus A319", num_rows = 22, num_seats_per_row=6))
     assert vuelo.num_available_seats() == 21 * 6

def test_num_available_seats_menos_uno():
    vuelo = flight.Flight(number = "BA117", aircraft = Aircraft(registration = "G-EUAH", model = "Airbus A319", num_rows = 22, num_seats_per_row=6))
    p1 = Passenger("Jack", "Shephard", "85994003S")
    vuelo.allocate_passenger("12A", p1.passenger_data())
    assert vuelo.num_available_seats() == (21 * 6) - 1

