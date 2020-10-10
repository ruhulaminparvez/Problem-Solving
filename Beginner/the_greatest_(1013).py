value = input().split(" ")

a, b, c = value

calc = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
result = (int(calc) + int(c) + abs(int(calc) - int(c)))/2

print("%d eh o maior" %result)


