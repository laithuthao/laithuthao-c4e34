
fav =["death note", "netflix", "football"]
print("Here your fav so far:", *fav, sep=", ")
new=input("anything:")
fav.append(new)
print(*fav, sep=", ")

