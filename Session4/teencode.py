code = {
    "hc": "hoc",
    "ng": "nguoi",
    "pt": "phat trien",
    "eny": "em nguoi yeu",
    "any": "anh nguoi yeu"
}

while True:

    for key in code.keys():
        print(key, end=" ")
    print()

    a=input("Your code?")
   
    if a in code:
        print(code[a])

    else:
        b=input("No value. Do you want to input?").upper()
        if b == "Y":
            d=input("Meaning?")
            code[a]=d

        else:
            print("Good bye!")
            break
