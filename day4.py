number=int(input("Enter N values:"))
a=[]
for i in range(number):
    a.append(i)
print(a)
#adding item to list
a.insert(5,7)
print(a)
#removing item from list
a.pop(8)
print(a)
#largest value
print(max(a))
#smallest value
print(min(a))

#create and reverse a tuple
x=(1,2,3,4,5)
y=reversed(x)
print(tuple(y))

#convert tuple to list
b=list(x)
b[2]=4
x=tuple(b)
print(x)