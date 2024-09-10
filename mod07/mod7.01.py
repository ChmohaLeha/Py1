kk = ("Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", "Heinäkuu", "elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")
luku = int(input("Anna kuukauden luku (1-12): "))
luku1 = kk[luku-1]
for i in range(luku):
    if luku == 12 or luku == 1 or luku == 2:
        print(f"Kuukausi {luku1} on talvi")
        break
    if luku == 3 or luku == 4 or luku == 5:
        print(f"Kuukausi {luku1} on kevät")
        break
    if luku == 6 or luku == 7 or luku == 8:
        print(f"Kuukausi {luku1} on kesä")
        break
    if luku == 9 or luku == 10 or luku == 11:
        print(f"Kuukausi {luku1} on syksy")
        break

