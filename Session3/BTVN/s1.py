menu = ["T-shirt", "Sweater"]

while True:
    i=input("Welcome to our shop, what do you want (C, R, U, D)?")
    if i in ["R","r"]:
        print("Our items: ", end="")
        print(*menu, sep=", ")

    elif i in ["C", "c"]:
        a=input("Enter new item: ")
        menu.append(a)
        print("Our items: ", end="")
        print(*menu, sep=", ")

    elif i in ["U", "u"]:
        c=int(input("Update position? "))
        d=input("New item: ")
        menu[c-1]=d
        print("Our items: ", end="")
        print(*menu, sep=", ")

    elif i in ["D", "d"]:
        e=int(input("Delete position? "))
        del menu[e-1]
        print("Our items: ", end="")
        print(*menu, sep=", ")

    else:
        break

