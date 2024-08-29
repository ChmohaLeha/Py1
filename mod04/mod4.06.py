# π≈4n/N jossa n on osuvat alueelle pisteet ja N on kaikki pisteet
# epäyhtälö x^2+y^2<1 testaa yksittäisen pisteen ympyrässä
import math
import random
N= int(input("Anna pisteiden lukumäärä: "))
counter = 0
n = 0
while counter < N:
    counter += 1
    x = random.random() * 2 - 1
    y = random.uniform(-1, 1)
    print(f"Satunnainen piste: {x}, {y}")
    print(x**2 + y**2 < 1)
    if x**2 + y**2 < 1:
        print("Osui ympyrän sisälle.")
        n=n+1
print(f"{N} pisteestä {n} osui yksikköympyrän sisälle.")
vast = 4 * n / N
print(f"Piin likiarvo on {vast}")
print(f"Virhe verrattuna math.pi ({math.pi}): {vast - math.pi:.5f}")







