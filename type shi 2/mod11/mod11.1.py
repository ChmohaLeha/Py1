class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulost(self):
        print(f"{self.nimi}")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoit, sivu):
        self.kirjoit = kirjoit
        self.sivu = sivu
        super().__init__(nimi)

    def tulost(self):
        super().tulost()
        print(f"Kirjoittaja ja sivut: {self.kirjoit}, {self.sivu}")

class Lehti(Julkaisu):
    def __init__(self, nimi, paajulk):
        self.paajulk = paajulk
        super().__init__(nimi)

    def tulost(self):
        super().tulost()
        print(f"Lehden pääjulkaisija: {self.paajulk}")

julkaisut = []
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))

for i in julkaisut:
    i.tulost()