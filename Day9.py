#LAMBDA

#multiplication
a=lambda x,y:x*y
print(a(12,2))

#Fibonacci series
from functools import reduce
fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
n = int(input())
print(fib(5))

#multiplying with given num
b=int("enter num:"input())
list1=[12,10,8,6]
list2=list(map(lambda x:x*n,list1))
print(list2)

#nums divisible by 9
lst=[4,9,18,45,50,36]
lst2=list(filter(lambda x:x%9==0,lst))
print("filtered list:",lst2)

#even nums in a list
lst=[3,23,4,5,6,75,88,19,56,43,89]
count=0
lst2=list(filter(lambda x:x%2==0,lst))
print("count of even nos. in the list:",len(lst2))