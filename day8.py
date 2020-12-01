#try block
try:
    list1=[]
    n=int(input("Enter n:"))
    for i in range (0,n):
       value=int(input())
       list1.append(value)
    print(list1)
    print("enter index to be popped:")
    pop_ind=int(input())
    list1.pop(pop_ind)
    print(list1)
except Exception as e:
    print(e)

#try-except
#It’s executed when there are no exceptions raised by the try block.
def divide(x, y):
    try:
        print(f'{x}/{y} is {x / y}')
    except ZeroDivisionError as e:
        print(e)
divide(10, 2)
divide(10, 0)
divide(10, 4)

#NameError
try:
    num1=int(input())
    num2= int(input())
    marks = num1/num2
    print(marks)
    print(stud,marks)

except NameError as ne:
    print("name error is caused ",ne)
except Exception as e:
    print(e)

#calculator app
def add(a,b):
    c=a+b
    print(c)
def sub(a,b):
    c=a-b
    print(c)
def mul(a,b):
    c=a*b
    print(c)
def div(a,b):
   try:
    c=a/b
    print(c)
   except Exception as e:
       print("Exception caused:",e)


def enterinput():
    try:
        num1=int(input())
        num2=int(input())
        operator=input()
        if operator=='+':
           add(num1,num2)
        elif operator=='-':
            sub(num1,num2)
        elif operator == '*':
          mul(num1, num2)
        elif operator == '/':
             div(num1, num2)
        else:
              print("wrong input")
              enterinput()
    except Exception as e:
        print("Exception raised :",e)
    finally:
        enterinput()
enterinput()

#errors
from math import cube       #import error

import cube         #module not found error

stud={1:"loey",2:"bbh",3:"kai"}
print(stud[4])      #key error

list1=[90,40,45]
print(list1[3])     #index error

marks=max(list1)
if marks<40:
    div=marks/0     #Zerodivision error
    print(div)
elif marks>40 | marks<80 :
    div=marks/2
    print(div)
else                #syntax error
    div=marks
    print(div)

print(name)         #name error

age=2
print('age'+2)      #type error