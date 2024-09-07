import math
def calc(dim, hint):
    dim = dim / 100
    # pi * r^2
    r = dim/2
    ar = math.pi * r ** 2
    return hint/ar

halk = float(input("Syötä 1. pizzan halkasija (cm): "))
halk2 = float(input("Syötä 2. pizzan halkasija (cm): "))
maks1 = float(input("Syötä 1. pizzan hinta: "))
maks2 = float(input("Syötä 2. pizzan hinta: "))

nelihint = calc(halk, maks1)
nelihint1 = calc(halk2, maks2)

print(f"Ensimmäisen pizzan neliö hinta on {nelihint:.2f}")
print(f"Toisen pizzan neliö hinta on {nelihint1:.2f}")

if nelihint < nelihint1:
    print("Eka pizza on neliöhintaan halvempi")

elif nelihint > nelihint1:
    print("Toinen pizza on neliöhintaan halvempi")
else:
    print("Pizzojen neliöhinta on sama")

"""
print(calc(100, 30))
print(calc(30, 20))
"""