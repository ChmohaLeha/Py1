"""
import random
diel = idel = count = 0
while diel != 6 or idel != 6:
    diel = random.randint(1,6)
    idel = random.randint(1, 6)
    count += 1
    print(f"Nopan silmäluku: {diel}, heittojen lkm: {count}")
print(f"Heittojen lkm: {count}")
"""
tuuma = int(input("Anna tuuma määrä: ")) * 2.54
while tuuma:
    if tuuma < 0:
        print("Älä syötä negatiivisia lukuja")
        break
    elif tuuma > 1:
        print(f"Vastaus senttimetreinä: {tuuma}")
        tuuma = int(input("Anna tuuma määrä: ")) * 2.54
    else:
        print("Varmista oikea syöttö")




