print("enter the number corresponding to the command of your choice \n 1.add \n 2.subtract \n 3.divide \n 4.multiply")
c=int(input("enter your choice"))
a=int(input("enter first number:"))
b=int(input("enter second number:"))
def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def mult(x,y):
    print(x*y)
def div(x,y):
    print(x/y)
while c<1 or c>4:
    c=int(input("please enter a valid choice:"))
if c==1:
    add(a,b)
elif c==2:
    sub(a,b)
elif c==3:
    div(a,b)
else:
    mult(a,b)
        
        
        
                
          
