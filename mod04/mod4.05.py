command = input("Käyttäjätunnus: ")
command2 = input("Salasana: ")
rep = 0
while rep <4:
    if command == "python" and command2 == "rules":
        print("Tervetuloa")
        break
    elif command != "python" or command2 != "rules":
        print("Yritä uudelleen")
        command = input("Käyttäjätunnus: ")
        command2 = input("Salasana: ")
        rep = rep + 1
print("Pääsy evätty")










