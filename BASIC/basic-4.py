num=int(input("enter a num "))

check=True
for i in range(2,num//2+1):
    if(num%i==0):
        check=False
if(check):
    print("yes num is prime")
else:
    print("no num is not prime")
        
        
