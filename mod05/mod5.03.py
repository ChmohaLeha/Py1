alkuluku = True
tutkittava = int(input("Anna tutkittava luku: "))
for jakaja in range(2, tutkittava):
    if tutkittava % jakaja == 0:
        alkuluku = False
        print("lukusi ei ole alkuluku")
        break
if alkuluku:
    print("Lukusi on alkuluku") 
