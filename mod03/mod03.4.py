vuos = int(input("Kirjoita vuosi: "))
if vuos % 400 == 0:
    print("Vuosi on karkaus vuosi")
elif (vuos % 100 == 0):
    print("Vuosi ei ole karkaus vuosi")
elif (vuos % 4 == 0):
    print("Vuosi on karkaus vuosi")
else:
    print("Vuosi ei ole karkausvuosi")
