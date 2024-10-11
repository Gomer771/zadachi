n=int(input())
n=int(n)
sum=0
if n>=0:
    for i in range(1,n+1):
        sum=sum+i
else:
    for i in range(n, 2) :
        sum=sum+i
b=str(sum)
print(b)