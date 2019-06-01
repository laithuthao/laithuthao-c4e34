fav =["death note", "netflix", "football"]
print("Here your fav so far:")
print(*fav, sep=" , ")

for index, value in enumerate(fav):
    print(index+1, value)
