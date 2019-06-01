yob=int(input("Year of birth?"))
age=2019-yob
print(age)

if age<10:
    print("Baby")
elif age<18:
    print("Teenager")
elif age<25:
    print("Adolescent")
else:
    print("Adult")