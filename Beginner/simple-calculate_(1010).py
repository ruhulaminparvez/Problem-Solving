input1 = input().split(" ")
input2 = input().split(" ")

cod1, q_prod1, price1 = input1
cod2, q_prod2, price2 = input2

total = (int(q_prod1) * float(price1)) + (int(q_prod2) * float(price2))

print("VALOR A PAGAR: R$ %0.2f" %total)