import random
luku = int(input("Anna luku 1-10: "))
die = random.randint(1,10)
while luku:
    if luku == die:
        print("Oikein viotit pelin!")
        break
    elif luku > die:
        print("Liian suuri arvaus")
        luku = int(input("Anna luku 1-10: "))
    elif luku < die:
        print("Liian pieni arvaus")
        luku = int(input("Anna luku 1-10: "))
    else:
        print("Väärä syöttö")
        break



