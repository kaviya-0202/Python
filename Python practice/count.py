n = int(input("enter the number:"))
count=0
i=1
while i<=n:
    if i%7 ==0:
        count = count+1
    i = i+1
print(count)