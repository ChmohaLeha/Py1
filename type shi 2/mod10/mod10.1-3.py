class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros > self.ylin_kerros or kohde_kerros < self.alin_kerros:
            print(f"Kerrosta {kohde_kerros} ei ole olemassa.")
            return

        print(f"Hissi siirtyy kerrokseen {kohde_kerros}.")

        if self.nykyinen_kerros < kohde_kerros:
            while self.nykyinen_kerros < kohde_kerros:
                self.kerros_ylos()
        elif self.nykyinen_kerros > kohde_kerros:
            while self.nykyinen_kerros > kohde_kerros:
                self.kerros_alas()

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.hissit = []

        for i in range(hissien_lkm):
            uusi_hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)

    def aja_hissia(self, hissi_numero, kohde_kerros):
        if hissi_numero > len(self.hissit) or hissi_numero < 1:
            print("Virhe: hissiä ei ole olemassa.")
        else:
            valittu_hissi = self.hissit[hissi_numero - 1]
            valittu_hissi.siirry_kerrokseen(kohde_kerros)

    def palohal(self):
        print("\nPalohälytys! Kaikki hissit siirtyvät pohjakerrokseen.")
        for idx, hissi in enumerate(self.hissit, start=1):
            print(f"\nHissi {idx} siirtyy pohjakerrokseen.")
            hissi.siirry_kerrokseen(self.alin_kerros)

if __name__ == "__main__":
    talo = Talo(1, 9, 3)
    talo.aja_hissia(1, 7)
    talo.aja_hissia(2, 5)
    talo.aja_hissia(3, 9)

    talo.palohal()
