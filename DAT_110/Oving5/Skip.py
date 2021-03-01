class Slagskip:
    #Oppretter skip
    def __init__(self, start_x, start_y,  lengde, retning="horisontal"):
        self.retning = retning
        self.lengde = lengde
        self.antalltreff = 0
        if self.retning == "horisontal":
            self.skip = [(start_x, start_y)]
            x = start_x
            y = start_y
            for i in range(1,lengde,1):
                x += 1
                self.skip.append((x,y))

    # Sjekker om den treffer
    def treff(self, koordinat):
        if koordinat in self.skip:
            self.antalltreff +=1
            return True

    # Returner punkt og lengde og antall treff
    def __str__(self):
        return f"Punkt: ({self.skip}, Lengde: {self.lengde}, Antall treff: {self.antalltreff})"

    # Sjekker om skipet har blitt senka
    def er_senket(self, lengde=2):
        if self.antalltreff == lengde:
            return True
        else:
            return False



if __name__ == "__main__":
    skip1 = Slagskip(4,2,2) # Oppretter skip 1
    skip2 = Slagskip(6,3,4) # Skip nr2
    antalltreff_skip1 = 0
    antalltreff_skip2 = 0
    brukte_koordinater1 = []
    brukte_koordinater2 = []

    while skip1.er_senket() == False or skip2.er_senket() == False:
        koordinater = input("Spiller 2, skyt: ").split()
        koordinat = tuple([int(j) for j in koordinater])
        while koordinat in brukte_koordinater1:
            koordinater = input("Brukte koordinater, prøv på ny: ").split()
            koordinat = tuple([int(j) for j in koordinater])
        resultat = skip1.treff(koordinat)
        if resultat == True:
            antalltreff_skip1 += 1
        print(f"Antall treff skip nr1:  {antalltreff_skip1}")
        if antalltreff_skip1 == skip1.lengde:
            print("-"*25)
            print("Spiller 2 vant")
            print(f"Skip nummer 1: {skip1}")
            break
        brukte_koordinater1.append(koordinat)
        print("")

        # Spiller nr 1 får gjette
        koordinater = input("Spiller 1, skyt: ").split()
        koordinat = tuple([int(j) for j in koordinater])
        while koordinat in brukte_koordinater2:
            koordinater = input("Allerde skoten, prøv på ny: ").split()
            koordinat = tuple([int(j) for j in koordinater])
        resultat = skip2.treff(koordinat)
        if resultat == True:
            antalltreff_skip2 += 1
        print(f"Antall treff skip nr2:  {antalltreff_skip2}")
        if antalltreff_skip2 == skip2.lengde:
            print("-"*25)
            print("Spiller 1 vant")
            print(f"Skip nummer 2: {skip2}")
            break
        brukte_koordinater2.append(koordinat)
        print("")
