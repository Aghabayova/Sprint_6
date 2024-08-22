from data import OrderData
import random


def generate_name():
    return random.choice(OrderData.name)


def generate_lastname():
    return random.choice(OrderData.lastname)


def generate_address():
    return random.choice(OrderData.address)


def generate_station():
    return random.choice(OrderData.station)


def generate_phone():
    number = random.randint(1111111, 9999999)
    return f'8916{number}'


def generate_rental_period():
    return random.choice(OrderData.rental_address)


def generate_color():
    return random.choice(OrderData.color)


def generate_comment():
    return random.choice(OrderData.comment)
