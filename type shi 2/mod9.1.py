import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        kuljettu = self.nopeus * tuntimaara
        self.kuljettu_matka += kuljettu

autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu_kaynnissa = True
tunti = 0


while kilpailu_kaynnissa:
    tunti += 1
    print(f"\nTunti {tunti}:")

    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)
        auto.kulje(1)

        print(f"{auto.rekisteritunnus}: nopeus {auto.nopeus} km/h, kuljettu matka {auto.kuljettu_matka:.1f} km")

        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False
            break


print("\nKilpailu on päättynyt. Tulokset:\n")
print(f"{'Rekisteritunnus':<15}{'Huippunopeus (km/h)':<20}{'Nopeus (km/h)':<15}{'Kuljettu matka (km)':<20}")
print("-" * 70)

for auto in autot:
    print(f"{auto.rekisteritunnus:<15}{auto.huippunopeus:<20}{auto.nopeus:<15}{auto.kuljettu_matka:<20.1f}")

