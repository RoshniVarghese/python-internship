#adding 2 num
list1=[1,2,3,4,5]
list2=[]
for  i in list1:
  a=i+2
  list2.append(a)
print(list2)

#pattern pgm
for i in range(5,0,-1):
  print("".join(format(j)   for j in range(i,0,-1)))

#Fibonacci sequence
def fibonacci(a):
  num1=0
  num2=1
  if a==0:
    print(num1)
  elif a<0:
    print("Enter positive value")
  else:
    for i in range(a):
      print(num1)
      num3=num1+num2
      num1=num2
      num2=num3
number=int(input("Enter the number(fibonacci):"))
fibonacci(number)

#Armstrong number
def amstrong(num) :
    sum = 0
    temp = num
    order=len(str(num))
    while num > 0 :
        digit = num % 10
        sum += digit ** order
        num //= 10

    if sum == temp :
        print(f"{sum} is Amstrong Number")
    else :
        print("Number is not  Amstrong Number")


num = int(input("Enter the number (Amstrong):"))
amstrong(num)

#multiplication table of 9
def tables9():
  val=int(input("Enter value(tables):"))
  for i in range(1,val+1):
    print(f"9 x {i} = {9*i}")
tables9()

#checking if +ve or -ve
def check(value):
  if value<0:
    print("Negative")
  elif value==0:
    print("Zero")
  else:
    print("Positive")
check(9)
check(-5)

#convert the number of days to ages
def ages(days):
  year=int (days/365)
  print(f"{year} Year")
ages(int(input("Enter no.of.days:")))

#Trigonometry problem
import math as m
a=m.sin(1/4)
b=m.cos(1/4)
sum = a**2+ b**2
print(round(sum))

#calculator
def calculator(a,b):
    val=int(input("What you want to do?\n1.add\n2.sub\n3.divide\n4.multiplication\nEnter your choice \t"))
    if val==1:
      print(f"The sum of a and b :{a+b}")
    elif val==2:
      print(f"The difference of a and b:{a-b}")
    elif val==3:
      print(f"The division of a and b:{a//b}")
    elif val==4:
      print(f"The multiplication of a and b:{a*b}")
    else:
      print("invalid")
a=int(input("Enter the a value (calculator):"))
b=int(input("Enter the b value (calculator):"))
calculator(a,b)