import matplotlib.pyplot as plt

intervall = int(input("Tidsintervall: "))
antall_intervaller = int(input("Antall intervaller: "))

# Kunne hatt disse tomme men 0 gjør at dem starter på 0 og ikkje på første intervall.
y_distanse = [0]
x_tid = [0]
y_fart = [0]
for tid in range(intervall, antall_intervaller*intervall+intervall, intervall):
    akselerasjon = 9.81
    fart = akselerasjon * tid
    distanse = 0.5 * fart * tid
    y_distanse.append(distanse)
    x_tid.append(tid)
    y_fart.append(fart)

plt.plot(x_tid,y_distanse,"o", label="Distanse")
plt.plot(x_tid,y_fart, "r", label="Fart")
plt.grid(True)
plt.legend(loc=2)
plt.ylabel("Distanse falt")
plt.xlabel("Tid")
plt.show()
