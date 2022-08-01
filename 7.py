Prime_Numbers=[]
Count=0
i=2
Statement=True
while Statement:
    j=i-1
    while j>=2 and i%j!=0:
        Count=Count+1
        j=j-1
    if Count == i-2:
        Prime_Numbers.append(i)
    Count=0
    i+=1
    if len(Prime_Numbers)==10001:
        Statement=False
print(max(Prime_Numbers)) and i%1==0: