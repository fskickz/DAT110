import delelig as dele
import perfekttall as perf

#Sjekker om tall A er delelig på B
a = int(input("Tall A:"))
b = int(input("Tall B:"))
print(str(a) + " er delelig med " + str(b) + " : " + str(dele.delelig(a,b)))

#Sjekker om tallet er perfekt
tall = int(input('Et nytt tall:'))
print(str(tall) + " er et perfekt tall: " + str(perf.perfekttall(tall)))
