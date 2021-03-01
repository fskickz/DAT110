# Oppgave 1d
intervall = int(input("Tidsintervall: "))
antall_intervaller = int(input("Antall intervaller: "))

for tid in range(intervall, antall_intervaller*intervall+intervall, intervall):
    akselerasjon = 9.81
    fart = akselerasjon * tid
    distanse = 0.5 * fart * tid
    print("Farten er " + str(fart) + " m/s og distansen er " + str(distanse) + " meter")
