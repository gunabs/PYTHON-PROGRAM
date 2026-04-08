def add(a,b):
   print(a+b)
def sub(a,b):
   print(a-b)
def mul(a,b):
   print(a*b)
def div(a,b):
    if b!=0:
     print(a//b)
    else:
        print("wrong division by zero")

print("enter which operation do 1.add,2.sub,3.div,4.mul")
operation =input("enter operation").strip()
a=int(input("enter a value"))
b=int(input("enter b value"))

if operation=="add":
    add(a,b)
elif operation=="sub":
    sub(a,b)
elif operation=="mul":
    mul(a,b)
elif operation=="div":
    div(a,b)
else:
    print("you enter erong option")


        
        
