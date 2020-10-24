N = int(input())

a = N / 365;
rA = N % 365;
rM = rA % 30;
m = rA / 30;
d = rM % 30;

print("%d ano(s)" % a)
print("%d mes(es)" % m)
print("%d dia(s)" % d)
