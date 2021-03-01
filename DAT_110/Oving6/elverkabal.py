import DAT_110.klasser.kortspill as kortspill
import time

class Spill:
    def __init__(self):
        self.kort = kortspill.Kortstokk()
        self.liste = []
        self.kort.stokk()
        self.ulovligInput = False
        for i in range(9):
            trekkte_kort = self.kort.trekk()
            self.liste.append(trekkte_kort)

    def skriv_tilstand(self):
        plass = 0
        print("")
        for j in self.liste:
            print(f"Plass {plass} inneholder: {j}")
            plass += 1
        print(f"Kort igjen: {len(self.kort.kortene)} ")
        print("")

    def plasser_to_kort(self, index1, index2):
        if self.liste[index1].verdi + self.liste[index2].verdi == 11:
            trekkt_kort = self.kort.trekk()
            self.liste[indeks1] = trekkt_kort
            trekkt_kort = self.kort.trekk()
            self.liste[indeks2] = trekkt_kort
        else:
            print("Det er ikkje lovleg input, game over")
            time.sleep(3)
            self.ulovligInput = True

    def plasser_tre_kort(self, index1, index2, index3):
        if (self.liste[index1].verdi >= 11 and self.liste[index2].verdi >= 11 and
            self.liste[index3].verdi >= 11):
            trekkt_kort = self.kort.trekk()
            self.liste[indeks1] = trekkt_kort
            trekkt_kort = self.kort.trekk()
            self.liste[indeks2] = trekkt_kort
            trekkt_kort = self.kort.trekk()
            self.liste[indeks3] = trekkt_kort
        else:
            print("Du har ikkje tre bildekort, game over")
            time.sleep(3)
            self.ulovligInput = True

    def er_spill_ferdig(self):
        if len(self.kort.kortene) == 0 or self.ulovligInput == True:
            return True
        else:
            return False


if __name__ == "__main__":
    kabal = Spill()
    while kabal.er_spill_ferdig() == False:
        kabal.skriv_tilstand()
        hvor_mange_kort = int(input("Hvor mange kort vil du legge ut? "))
        if hvor_mange_kort >= 2 and hvor_mange_kort <= 3:
            indeks1 = int(input("Kortplass nr: "))
            indeks2 = int(input("Kortplass nr: "))
            if hvor_mange_kort == 2:
                kabal.plasser_to_kort(indeks1,indeks2)
            elif hvor_mange_kort == 3:
                indeks3 = int(input("Kortplass nr: "))
                kabal.plasser_tre_kort(indeks1,indeks2,indeks3)
        else:
            kabal.ulovligInput = True
