print('''
Guess your number game
Now think of a number form 0 to 100, then press 'Enter'

All you have to do is to answer to my Guess
'c' if my guess is "C" correct
's' if my guess is "S"maller than you number
'l' if my guess is "L"arger than you number)
''')

low=0
high=101

while True:
    mid=(low+high)//2

    answer=input("Is {0} your number?".format(mid))

    if answer == 'l':
        high=mid
    elif answer == 's':
        low=mid
    elif answer == 'c':
        print("I knew it!")
        break