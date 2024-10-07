from random import randrange

def task_1(): # Lottery ticket generator

    ticket = []

    # Code here
    for i in range(6):
        ticket.append(randrange(1, 50))
    return ticket

def task_2(): # Countdown

    output = []

    # Code here
    number = int(input("Enter a number lower than 100: "))
    countdown = 100
    for i in range(countdown - number + 1):
        output.append(countdown)
        #print(countdown)
        countdown -= 1
    return output

def task_3():
    people_cars = {
        "Adam": "Volvo",
        "Kate": "BMW",
        "Mark": "BMW",
        "Hannah": "Ford",
        "Max": "Volvo",
        "Celine": "Fiat"
    }

    car_make_lengths = {}

    # Code here
    car_make_lengths2 = []
    i = 0
    for car in people_cars.values():
        x = len(car)
        if not x in car_make_lengths2:
            car_make_lengths2.append(x)
    car_make_lengths = car_make_lengths2
    return car_make_lengths