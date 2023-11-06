x = input().split(" ")

A,B,C = x

triangle = (float(A)*float(C))/2
print("TRIANGULO: %.3f"%(triangle))

pi = 3.14159
circle = (float(C)*float(C)*pi)
print("CIRCULO: %.3f"%(circle))

trapezium = float(C) *(float(A) + float(B)) / 2
print("TRAPEZIO: %.3f"%(trapezium))

square = (float(B)*float(B))
print("QUADRADO: %.3f"%(square))

rectangle = (float(A)*float(B))
print("RETANGULO: %.3f"%(rectangle))