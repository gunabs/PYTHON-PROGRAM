#adding five odd numbers
a=[10,15,20,25,30]

for i,x in enumerate(a):
    if x%2!=0:
        a[i]+=5
print(a)        
#using slicing to change items 
a=[1,2,3,4,5]
a[2:4]=[6:7]
print(a)
