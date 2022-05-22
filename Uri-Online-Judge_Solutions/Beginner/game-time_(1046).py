#Problem - 1043 (Game Time)
A, B = list(map(int, input().split()))

if(A<B):
    time=B-A
else:
    time=B+24-A

# print(f"O JOGO DUROU {time} HORA(S)")
print("O JOGO DUROU {} HORA(S)" .format(time))