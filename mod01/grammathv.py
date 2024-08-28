command = input("Monta leiviskää: ")
command2 = input("Monta naulaa: ")
command3 = input("Monta luotia: ")
leivis = float(command)
naulaa = float(command2)
luotia = float(command3)
leivi1 = leivis * 20
naula1 = (naulaa + leivi1) * 32
luotia1 = (luotia + naula1) * 13.3
kilo = (luotia1 / 1000)
kra1 = int(kilo)
gramma = (kilo - kra1) * 1000
print(f"Massa nykyisten mittojen mukaan:\n {kra1:.0f} kg ja {gramma:.2f} g")



