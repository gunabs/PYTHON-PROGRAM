
stri=input("enter string :")
size=len(stri)
print(size)
v=c=0

for i in range(0,size):
    if(('A'<=stri[i]<='Z') or ('a'<= stri[i]<='z')):
        if(stri[i] in "aeiouAEIOU"):
            v+=1
        else:
            c+=1

print("vowels :"+str(v))
print("constant :"+str(c))

            

    
