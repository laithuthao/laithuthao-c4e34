from random import randint, choice
x = randint(0,9)
y = randint(1,9)
error = choice([-1,0,0,0,0,0,1])
notice = ""

op=choice(["+", "-", "*", "/"])

#Way1:
from calc import eval
result=eval(x,y,op)
#Way2:
import calc
result=calc.eval(x,y,op)



hienthi=result+error

# print(x, op, y, "=", hienthi)

print("{0} {1} {2} = {3}".format(x,op,y,hienthi))

doan=input("Y/N?").lower()

if notice == "":
    if error==0:
        if doan=="y":
            print("You're right")
        else:
            print("Wrong")

    else:
        if doan=="y":
            print("Wrong")
        else:
            print("Right")
else:
    print(notice)