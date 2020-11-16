N = int(input());
Hour = Min = Sec = Num = 0
Num = N

Hour = N / 3600
Min = N % 3600 / 60
Sec = N % 60
        
print("%d:%d:%d" %(Hour,Min,Sec))




