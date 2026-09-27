n = int(input("enter the number:"))
i=2
is_prime = True
while i<n:
    if n%i ==0:
        is_prime=False
    i=i+1
if(is_prime):
     print(" prime")
else:
    print(" not a prime")