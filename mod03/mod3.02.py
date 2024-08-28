from Tools.scripts.var_access_benchmark import B

hyt = (input("Hyttiluokka? LUX, A, B vai C? : "))
if hyt=="LUX":
    print("Parvekkeellinen hytti yläkannella")
elif hyt=="A":
    print("Ikkunallinen hytti yläpuolella")
elif hyt=="B":
    print("Ikkunaton hytti puolella")
elif hyt=="C":
    print("Ikkunaton hytti alapuolella")
else:
    print("Virheellinen hytti")


