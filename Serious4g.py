n=int(input("The number of star in a row: "))
m=int(input("The number of row: "))

for i in range (1,m+1):
    for j in range (1,n+1):
        print("*", end=" ")
    print()