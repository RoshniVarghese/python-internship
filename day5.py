def my_fun(a,b):
    sum=a+b
    print("Adding a and b:" +str(sum))
    diff=a-b
    print("Subracting a and b:" +str(diff))
    div=a//b
    print("Dividing a and b:" +str(div))
    mul=a*b
    print("Multiplying a and b:" +str(mul))
a=int(input("Enter an Integer:"))
b=int(input("Enter an Integer:"))
my_fun(a,b)

def covid(name,temp=98):
    print("Name:"+name)
    print("temp:"+str(temp))
covid("Ram")
covid("Sam",98.8)