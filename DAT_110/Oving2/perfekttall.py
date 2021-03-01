def perfekttall(tall):
    import delelig as dele

    lengde = int(int(tall)/2+1)

    #1 til halvparten av tallet brukeren skriver inn
    faktorer = 0
    for i in range(1,lengde):
        # Dersom tallet er delelig med i, legg tallet til i faktorer
        if dele.delelig(tall,i):
            faktorer += i

    #Returner om summen av faktorer er lik tallet.
    return faktorer == tall


