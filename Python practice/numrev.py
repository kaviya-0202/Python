n = int(input("enter the number:"))
i=0
res=0
while i<=n:
    digit = n%10
    res =res*10+digit
    n=n//10
    i=i+1
print(res)