def gallon(gallona):
    return gallona * 3.785


def litr():
    while True:
        luku = int(input("Anna gallonan määrä (jos negatiivinen arvo ohjelma päättyy) : "))
        if luku < 0:
            print("ohjelma sammuu")
            break
        litroiksi = gallon(luku)

        print(f"{luku} litroina {litroiksi:.2f}")

litr()



