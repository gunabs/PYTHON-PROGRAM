num=int(input("enter a num"))
copy=num
sum=0
def fac(rem):
    fact=1;
    for i in range(1,rem+1):
        fact=fact*i
    return fact
        
while(copy):
    rem=copy%10
    sum=sum+fac(rem)
    
    copy//=10
if sum==num:
    print("its strong num")
else:
    print("its not a stron num")
    
    
