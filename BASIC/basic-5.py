num=int(input("enter a num "))
copy=num
sum=0

while copy:
    sum=(sum*10)+copy%10
    copy//=10
    
if(sum==num):
    print("yes num is palyndrom")
else:
    print("no num is not palyndrom")
        
        
