from random import randint
n=randint(0, 100)
print(n)

if n < 30:
    print("Sunny")
elif n < 70:
    print("Rainy")
else:
    print("Cloudy")
