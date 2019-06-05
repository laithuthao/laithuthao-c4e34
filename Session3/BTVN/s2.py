flock=[5,7,300,90,24,50,75]
print("Hello, my name is Hiep and these are my ship sizes", flock)

print("Now my biggest sheep has size", max(flock), "let's shear it")
m=max(flock)

while True:
    i=input(print("Do you want to shear it? Yes or No?"))
    if i in ["Yes", "yes", "Y", "y"]:
        flock[2]=8
        print("After shearing, here is my flock", flock)
        print("One month has passed, now here is my flock", flock)
        break
    elif i in ["No", "no", "N", "n"]:
        break
    else:
        break