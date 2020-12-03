#merge tuple from a list
state=["TamilNadu","Kerala","Karnataka"]
capital=["Chennai","Trivandrum","Bangaluru"]
zip_list=list(zip(state,capital))
print(zip_list)

#new tuple list
countries=["India","England","France","Finland","Iceland","Ireland","Italy","USA"]
new=list(zip(range(1,8),countries))
print(new)

#sorting a list
list1=[43,542,888,76,56,99,33,00,66,33,134]
print(sorted(list1))

#odd num
list2=[4,2,6,3,6,8,9,5,5,2,9,1,0,8,7]
odds=list(filter(lambda n: n%2!=0 , list2))
print(odds)