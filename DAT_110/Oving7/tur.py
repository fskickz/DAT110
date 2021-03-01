import math

class Posisjon:
    def __init__(self, x_koordinat, y_koordinat, hoyde):
        self.x_koordinat = x_koordinat
        self.y_koordinat = y_koordinat
        self.hoyde = hoyde

    def hoydeforskjell(self, annen_posisjon):
        return abs(self.hoyde - annen_posisjon.hoyde)

    def avstand(self, annen_posisjon):
        return math.sqrt((self.x_koordinat - annen_posisjon.x_koordinat)**2 +
                         (self.y_koordinat - annen_posisjon.y_koordinat)**2 +
                         (self.hoyde - annen_posisjon.hoyde)**2)

    def __eq__(self, other):
        if self.x_koordinat != other.x_koordinat:
            return False
        if self.y_koordinat != other.y_koordinat:
            return False
        if self.hoyde != other.hoyde:
            return False
        return True


class Tur:
    def __init__(self, navn, starttidspunkt, sluttidspunkt):
        self.navn = navn
        self.starttidspunkt = starttidspunkt
        if sluttidspunkt > starttidspunkt:
            self.sluttidspunkt = sluttidspunkt
        else:
            raise ValueError("Sluttidspunkt kan ikke være før starttidspunkt")
        self.posisjoner = list()

    def add_posisjon(self, posisjon):
        self.posisjoner.append(posisjon)

    def add_posisjon_koordinater(self, x_koordinat, y_koordinat, hoyde):
        self.posisjoner.append(Posisjon(x_koordinat, y_koordinat, hoyde))

    def hoydemeter(self):
        resultat = 0.0
        for i in range(1, len(self.posisjoner)): #Endret til 1,len...
            resultat += self.posisjoner[i-1].hoydeforskjell(self.posisjoner[i])
        return resultat

    def er_rundtur(self):
        if self.posisjoner[0] == self.posisjoner[-1]:
            return True
        return False

