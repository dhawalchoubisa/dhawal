a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if (a>=b)&(a>=c):
     print("a is greater",a);
elif(b>=c)&(b>=a):
     print("b is greater",b);
elif(c>=a)&(c>=b):
     print("c is greater",c);
else:
     print("invalid result")    

