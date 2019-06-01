

# from random import randint
# n=(randint(0, 100))
# print(n)

# while True:
#     i=int(input("Enter a number from 0 to 100: "))

#     if i > n:
#         print("too large")
#     elif i < n:
#         print("too small")
#     else:
#         print("bingo")
#         break



from random import randint
n=(randint(0, 100))
print(n)
loop=True
count=0

while loop:
    i=int(input("Enter a number from 0 to 100: "))
    count+=1
    if i > n:
        print("too large")
    elif i < n:
        print("too small")
    else:
        print("bingo")
        loop=False
    
    if count == 7:
        print("Game over")
        loop=False