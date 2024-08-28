suku = input("Sukupuoli? N tai M: ")
hemo = float(input("Hemoglobiinin arvo: "))
if suku == "N" and 117<=hemo<=175:
    print("Tasosi ovat normaaleja")
elif suku == "N" and 117>hemo:
    print("Tasosi ovat alhasia")
elif suku == "N" and hemo>175:
    print("Tasosi ovat korkeat")
if suku == "M" and 134<=hemo<=195:
    print("Tasosi ovat normaaleja")
elif suku == "M" and 134>hemo:
    print("Tasosi ovat alhasia")
elif suku == "M" and hemo>195:
    print("Tasosi ovat korkeat")
else:
    print("Virheellinen syöttö")




