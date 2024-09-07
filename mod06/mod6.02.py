import random

def noppa(taer):
    return random.randint(1, taer)
def hui():
    tahkot = int(input("Anna tahkojen lukumäärä: "))
    luku = 0
    while luku != tahkot:
        luku = noppa(tahkot)
        print(f"Heittosi: {luku}")


hui()