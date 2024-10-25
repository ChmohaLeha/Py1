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


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{'Rekisteritunnus':<15}{'Huippunopeus (km/h)':<20}{'Nopeus (km/h)':<15}{'Kuljettu matka (km)':<20}")
        print("-" * 70)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<15}{auto.huippunopeus:<20}{auto.nopeus:<15}{auto.kuljettu_matka:<20.1f}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0:
        print(f"\nTunti {tunti}")
        kilpailu.tulosta_tilanne()
print("\nKilpailu on päättynyt. Lopputulokset:\n")
kilpailu.tulosta_tilanne()

