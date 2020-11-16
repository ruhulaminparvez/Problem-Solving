a = int(input("Value for A: "))
b = int(input("Value for B: "))
c = int(input("Value for C: "))
d = int(input("Value for D: "))

sum1 = a+b
sum2 = c+d

if ((b > c) and (d > a) and (sum2 > sum1) and (c > 0) and (d > 0) and (a % 2 == 0)):
    print("Valores aceitos")

else:
    print("Valores nao aceitos")


