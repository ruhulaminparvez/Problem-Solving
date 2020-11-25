n1,n2,n3,n4 = map(float,input().split())
avg = (n1*2+n2*3+n3*4+n4*1)/10
print("Media: %.1f"%avg)
if avg>=7.0:
    print("Aluno aprovado.")
elif avg<5.0:
    print("Aluno reprovado.")
elif avg>=5.0 and avg<7.0:
    print("Aluno em exame.")
    N = float(input())
    print("Nota do exame: %.1f"%N)
    N = (avg+N)/2
    if N>=5.0:
        print("Aluno aprovado.")
        print("Media final: %.1f"%N)
    else:
        print("Aluno reprovado.")
        print("Media final: %.1f"%N)