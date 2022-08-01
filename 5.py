import math
from typing import *
a :List[int] =[]
b :List[List] =[]
for n in range(2,20):
    for i in range(2,20):
        while n%i==0:
            n=n/i 
            a.append(i)
    b.append(a)
    a=[]



print(b)
print(max(b))
       