import turtle

filreferanse = open("tegne_eksempel_2.txt", "r")

# Variabel som øker med 1 dersom det er eit flyttall
tallnr = 0
turtle.pensize(3)

# For hver linje i tekstfila
for tekst in filreferanse:
    try:
        tekst_tall = float(tekst)
        tallnr += 1
        #Dersom tallnr er delelig på 2 skal den tegne forover.
        if tallnr % 2 == 0:
            turtle.forward(abs(tekst_tall))
        #Viss ikkje er det vinkelen
        else:
            turtle.right(tekst_tall)

    # Dersom det ikkje er et flyttall skal det endres farge.
    except ValueError:
        tekst_s = tekst.strip()
        turtle.color(tekst_s)

turtle.done()
filreferanse.close()
