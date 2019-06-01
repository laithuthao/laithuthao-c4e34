fav =["death note", "netflix", "football"]

for index, value in enumerate(fav):
    print("{0}.{1}".format(index+1, value))

position=int(input("Position delete"))
del fav[position-1]

for index, value in enumerate(fav):
    print("{0}.{1}".format(index+1, value))