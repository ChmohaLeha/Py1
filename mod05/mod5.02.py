hui = []
luku = input("Anna luku tai paina Enter lopettaakseen: ")
while luku != "":
    hui.append(int(luku))
    luku = input("Anna luku tai paina Enter lopettaakseen: ")
for i in hui:
    hui.sort(reverse=True)
print(hui[:5])








