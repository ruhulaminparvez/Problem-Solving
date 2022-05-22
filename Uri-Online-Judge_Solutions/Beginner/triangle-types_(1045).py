#Problem - 1045 (Triangle Types)
A, B, C = list(map(float, input().split()))

if(A < B):
    temp = A
    A = B
    B = temp
if(B < C):
    temp = B
    B = C
    C = temp
if(A < B):
    temp = A
    A = B
    B = temp
    
if(A>=(B+C)):
    print("NAO FORMA TRIANGULO")
elif(A*A == (B*B+C*C)):
     print("TRIANGULO RETANGULO")
elif(A*A > (B*B+ C*C)):
    print("TRIANGULO OBTUSANGULO")
elif(A*A<(B*B + C*C)):
    print("TRIANGULO ACUTANGULO")
if(A == B and B == C):
        print("TRIANGULO EQUILATERO")
elif(A == B or B == C):
        print("TRIANGULO ISOSCELES")