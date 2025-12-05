print("enter two num :")
num_1=int(input("enter num-1 "))
num_2=int(input("enter num_2 "))
max=num_1
lcm=0
if(num_2>num_1):
    max=num_2
while True:
    if(max%num_1 ==0 and max%num_2==0):
        lcm=max
        break
    max+=1

print("the lcm :"+str(lcm))    
    
