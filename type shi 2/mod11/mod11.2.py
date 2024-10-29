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

class Sahko(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akku):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akku = akku

class Poltto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankki = tankki

sahkoaut = Sahko("ABC-15", 180, 52.5)
polttoaut = Poltto("ACD-123", 165, 32.3)

sahkoaut.nopeus = 150
polttoaut.nopeus = 120

sahkoaut.kulje(3)
polttoaut.kulje(3)

print("Autojen matkamittarilukemat kolmen tunnin ajon jälkeen:")
print(f"{sahkoaut.rekisteritunnus}: {sahkoaut.kuljettu_matka:.1f} km")
print(f"{polttoaut.rekisteritunnus}: {polttoaut.kuljettu_matka:.1f} km")
