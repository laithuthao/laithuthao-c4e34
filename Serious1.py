h=int(input("You height in cm: " ))
w=int(input("Your weight in kg: "))

i=h/100

B=w/(i*i)

if B<16:
    print("Severely underweight")
elif 16<=B<18.5:
    print("Underweight")
elif 18.5<=B<25:
    print("Normal")
elif 25<=B<30:
    print("Normal")
else:
    print("Obese")
