nimi = set()
while True:
    hui = input("Anna nimi tai Enter lopettaaksesi: ")

    if hui == "":
        break

    if hui in nimi:
        print("Aiemmin annettu nimi")
    else:
        print("Uusi nimi")
        nimi.add(hui)

for hui in nimi:
    print(hui)








