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




