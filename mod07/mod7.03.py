hui = {}
while True:
    print("1. Syötä uusi asema: ")
    print("2. Selaa lentoasemien tietoja: ")
    print("3. Lopeta: ")
    chlen = input(": ")
    if chlen == "1":
        koodit = input("Lentoaseman koodi: ").upper()
        nim = input("Lentoaseman nimi: ")
        if koodit in hui:
            print("Lentoasema on jo listassa")
        else:
            hui[koodit] = nim
            print(f"Lentoasema {nim} on listalla koodilla {koodit} ")
    elif chlen == "2":
        koodit = input("Syötä lentoaseman koodi: ").upper()

        if koodit in hui:
            print(f"Lentoaseman koodi on {koodit}: {hui[koodit]}")
        else:
            print(f"Lentoaseman koodilla {koodit} ei havaittu")

    elif chlen == "3":
        print("Lopetetaan ohjelma")
        break

    else:
        print("Virheellinen syöttö")


