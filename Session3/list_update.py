fav =["death note", "netflix", "football"]
print("Here your fav so far:")
print(*fav, sep=" , ")


a=int(input("position update: "))

b=input("Replace: ")

fav[a-1]=b

print(fav)
