#Problem - 1043 (Triangle)
a, b, c = list(map(float, input().split()))

if (a < b + c and b < a + c and c < a + b):
  print("Perimetro =", a+b+c)
else:
  print("Area =", (a+b)/2*c)