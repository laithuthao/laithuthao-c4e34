#Nhap 2 so. Nhan 2 so len roi lay tong chia 2. Xac dinh  so chan hay le

a=int(input("Nhap so thu nhat: "))
b=int(input("Nhap so thu hai: "))

x=a*b/2

if x%2 ==0:
    print("Day la so chan")
else:
    print("Day la so le")