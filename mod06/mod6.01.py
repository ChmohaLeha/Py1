import random

def noppa():
    return random.randint(1, 6)
def hui():
    luku = 0
    while luku != 6:
        luku = noppa()
        print(f"Heittosi: {luku}")


hui()




