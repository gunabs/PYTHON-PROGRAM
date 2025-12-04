#armstrong num

num=153
count=0
copy=num
def itsarmstrong(num,copy,count):
   check=num    
   while(copy):
      count+=1
      copy//=10

   sum=0
   while(num):
    sum=sum+(num%10)**count
    num//=10
   return sum==check
    

print(itsarmstrong(num,copy,count))



