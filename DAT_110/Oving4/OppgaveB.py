tekstfil = input("Navn på fila med eposter: ")

filreferanse = open(tekstfil, "r")

# Oppretter dictionary
domener = dict()

# Henter ut hver linje
for linje in filreferanse:
    linje_stripped = linje.strip()  # Fjerner mellomrom før og etter linja
    if linje_stripped.find("From:") != -1 and linje_stripped.find("@") != -1 and linje_stripped.find(">"):
        domene = linje_stripped[linje_stripped.find("@") + len("@"):linje_stripped.rfind(">")]
        if domene in domener:
            domener[domene] += 1
        else:
            domener[domene] = 1

# Print normal dictionary:
print("\nVanlig dict")
print("-"*20)
for domene in domener:
    print(f"{domene} : {domener[domene]}")


#############################
######### Frivillig #########
#############################

# Print sortert etter antall:
print("\nSortert etter antall")
print("-"*20)
sortAntall = {domenenavn: antall for domenenavn, antall in sorted(domener.items(),
                                                                  key=lambda item: item[1], reverse=True)}
for domene in sortAntall:
    print(f"{domene} : {domener[domene]}")

# Print sortert alfabetisk:
print("\nSortert alfabetisk")
print("-"*20)
sortAlfa = {domenenavn: antall for domenenavn, antall in sorted(domener.items(), key=lambda item: item[0])}
for domene in sortAlfa:
    print(f"{domene} : {domener[domene]}")



# Skriver alt til fil dersom ein vil sjå på det i txt
with open("Lister.txt", "w") as skrivfil:
    skrivfil.write("Normal liste \n")
    skrivfil.write("-"*20 + "\n")
    for domene in domener:
        skrivfil.write(f"{domene} : {domener[domene]} \n")
    skrivfil.write("\n Alfabetisk liste: \n")
    skrivfil.write("-"*20 + "\n")
    sortAlfa = {domenenavn: antall for domenenavn, antall in sorted(domener.items(), key=lambda item: item[0])}
    for domene in sortAlfa:
        skrivfil.write(f"{domene} : {domener[domene]} \n")
    skrivfil.write("\n Antall \n")
    skrivfil.write("-"*20 + "\n")
    sortAntall = {domenenavn: antall for domenenavn, antall in sorted(domener.items(),
                                                                  key=lambda item: item[1], reverse=True)}
    for domene in sortAntall:
        skrivfil.write(f"{domene} : {domener[domene]} \n")
