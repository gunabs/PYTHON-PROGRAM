num=(int)(input("enter a num"))
mul=num*num
sum=0
while(mul):
    sum=sum+(mul%10)
    mul//=10
if sum==num:
    print("its neon num")
else:
    print("its not a neon num")
    
    
