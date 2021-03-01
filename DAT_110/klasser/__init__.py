import random

class Kort:
    def __init__(self,type,verdi):
        self.type = type
        self.verdi = verdi

    def __str__(self):
        if self.verdi >= 1 and self.verdi <= 10:
            return f"{self.type} {self.verdi}"
        if self.verdi == 11:
            return f"{self.type} Knekt"
        if self.verdi == 12:
            return f"{self.type} Dame"
        if self.verdi == 13:
            return f"{self.type} Konge"
        return "ugyldig kort"


class Kortstokk:
    def __init__(self):
        self.kortene = []
        for i in range(1,14):
            self.kortene.append(Kort("Spar", i))
            self.kortene.append(Kort("Ruter", i))
            self.kortene.append(Kort("Kløver", i))
            self.kortene.append(Kort("Hjerter", i))

    def stokk(self):
        random.shuffle(self.kortene)

    def trekk(self):
        kortet = self.kortene[-1]
        del self.kortene[-1]
        return kortet

    def __str__(self):
        resultat = "Kortstsokk \n"
        for kort in self.kortene:
            resultat += str(kort) + "\n"
        return resultat

    def __len__(self):
        return len(self.kortene)

class Spiller:
    def __init__(self, navn, kort):
        self.navn = navn
        self.kort = kort

def finn_vinnere(spillere):
    vinnere = list()
    for spiller in spillere:
        if len(vinnere) == 0:
            vinnere.append(spiller)
            continue
        if spiller.kort.verdi > vinnere[0].kort.verdi:
            vinnere.clear()
            vinnere.append(spiller)
        elif spiller.kort.verdi == vinnere[0].kort.verdi:
            vinnere.append(spiller)
    return vinnere

if __name__ == "__main__":
    antall_spillere = int(input("Antall spillere:"))
    spillere = []
    kortstokken = Kortstokk()
    kortstokken.stokk()
    for i in range(antall_spillere):
        navn = input(f"Navn til spiller {i}: ")
        kortet = kortstokken.trekk()
        spilleren = Spiller(navn, kortet)
        spillere.append(spilleren)
    print("Status:")
    for spiller in spillere:
        print(f"Spiller {spiller.navn} har {spiller.kort}")
    vinnere = finn_vinnere(spillere)
    while len(vinnere) > 1:
        spillere = vinnere
        for spiller in spillere:
            spiller.kort = kortstokken.trekk()
            print(f"Spiller {spiller.navn} har {spiller.kort}")
        vinnere = finn_vinnere(spillere)

    print(f"Vinner er {vinnere[0].navn} med {vinnere[0].kort}")
