import math
n = 600851475143


for i in range(2,int(math.sqrt(n))):
    if n%i==0:
        n=n/i
       
        print(i)



