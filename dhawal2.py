name=input("enter your name")
roll_no=input("enter your roll_no")
adress=input("enter your adress")
a=int(input("enter the first subject marks"))
b=int(input("enter the second subject marks"))
c=int(input("enter the third subject marks"))
d=int(input("enter the fourth subject marks"))
e=int(input("enter the fifth subject marks"))
sum=(a+b+c+d+e)
avg=sum/5
percent=(sum*100)/500
print("percent is",percent)
print("avg is",avg)
if(avg>=90):
    print("grade a")
elif(avg>=80)&(avg<90):
    print("grade b")
elif(avg>=70)&(avg<80):
    print("grade c")
elif(avg>=60)&(avg<70):
    print("grade d")
            
