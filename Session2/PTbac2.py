a=int(input("Nhap bien thu nhat: " ))
b=int(input("Nhap bien thu hai: "))
c=int(input("Nhap bien thu ba: "))

d=b*b-4*a*c

if d<0:
    print("Vo nghiem")
elif d>0:
    print("2 nghiem phan biet, x1 = ", (-1*b-(0.5**d))/2*a, "x2 =", (-1*b+(0.5**d))/2*a)
else:
    print("Nghiem kep, x = ", -1*b/(2*a))


#elif d==0:
    x= -b/(2*a)
    print("Nghiem kep: {0}".format(x))

#elif d>0:
    x1= (-1*b-(0.5**d))/2*a
    x2= (-1*b+(0.5**d))/2*a
    print("2 nghiem phan biet: {0} va {1}".format(x1, x2))