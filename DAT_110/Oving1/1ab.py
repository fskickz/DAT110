# Oppgave 1ab
tid = int(input("Hvor lenge faller objektet?"))
if tid <= 0:
    tid = int(input('Skriv inn et gyldig tall over 0:'))
else:
    akselerasjon = 9.8
    fart = akselerasjon * tid
    distanse = 0.5 * fart * tid
    print("Farten er " + str(fart) + " m/s og distansen er " + str(distanse) + " meter")

