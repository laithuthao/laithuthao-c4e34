x=int(input('Enter a number'))
y=int(input("Another"))
op=input("Enter operator: ")
result = " "
notice = " "

if op == "+":
    result = x+y
elif op == "-":
    result = x-y
elif op == "/":
    if y==0:
        notice == "error"
    else:
        result = x/y
elif op == "*":
    result = x*y

print(result)
