import random
luku = int(input("Anna arpakuutioiden lukumäärä: "))
yht = 0
for vas in range(luku):
    comd = random.randint(1, 6)
    yht += comd

print(f"Kuutioiden lukumäärä summa on {yht}")



















