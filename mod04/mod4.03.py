num = []
while True:
    x = (input("Syötä luku: "))
    if x == "":
        break

    num.append(float(x))

if num:
    print("Suurin luku on: ", max(num))
    print("Pienin luku on: ", min(num))










