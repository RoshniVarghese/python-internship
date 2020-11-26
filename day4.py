numbers = [1,3,5,8,4,7,2,6,9]
print(numbers)
numbers.append(0)
print(numbers)
del numbers[4]
print(numbers)
x=max(numbers)
print(x)
y=min(numbers)
print(y)

p=reversed(numbers)
print(tuple(p))

a=list(numbers)
a[3]=4
numbers=tuple(a)
print(numbers)



