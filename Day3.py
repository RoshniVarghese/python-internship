d1 = {'p': 100, 'q': 200, 'r':400}
d2 = {'x': 300, 'y': 200, 'z':500}
d = d1.copy()
d.update(d2)
print(d)

d2.pop('z')
print(d2)

country = ['India', 'Australia', 'Pakistan']
captain = ['Virat_Kholi','Aaron_Finch', 'Babar_Azam']
cricket_dictionary = dict(zip(country, captain))
print(cricket_dictionary)

set1={"R","O","S","H","N","I"}
print(len(set1))

set2={"R","O","N","N","I","E"}
print (set1-set2)