n=[1,2]
sum=0
total=0
while True:
  n.append(n[-1]+n[-2])  
  if n[-1]>4000000:
    break
n.pop()
for i in n:
    if i%2==0:
        sum=sum+i
even = [x for x in n if x%2==0]
print(even)
for i in even:
    total+=i

print(total)