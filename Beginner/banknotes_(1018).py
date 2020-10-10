N = int(input())
Hundred = Fifty = Twenty = Ten = Five = Two = One = Num = 0
Num = N
while N != 0:
    if N >= 100:
        Hundred = N / 100
        N = N % 100
    elif N >= 50:
        Fifty = N / 50
        N = N % 50
    elif N >= 20:
        Twenty = N / 20
        N = N % 20
    elif N >= 10:
        Ten = N / 10
        N = N % 10
    elif N >= 5:
        Five = N / 5
        N = N % 5
    elif N >= 2:
        Two = N / 2
        N = N % 2
    else:
        One = N
        N = 0
print(Num)
print("%d nota(s) de R$ 100,00" % Hundred)
print("%d nota(s) de R$ 50,00" % Fifty)
print("%d nota(s) de R$ 20,00" % Twenty)
print("%d nota(s) de R$ 10,00" % Ten)
print("%d nota(s) de R$ 5,00" % Five)
print("%d nota(s) de R$ 2,00" % Two)
print("%d nota(s) de R$ 1,00" % One)

