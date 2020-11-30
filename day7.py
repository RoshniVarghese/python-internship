#importing module
import ex
print(ex.list1)

#pandas
import pandas as pd
a=["TamilNadu","Kerala","Karnataka"]
b=["Chennai","Trivandrum","Bangaluru"]
c=list(zip(a,b))
df=pd.DataFrame(data=c,columns=['State','Capital'])
print(df)

#random numbers
import random as rd
print ("Random Numbers:",rd.randint(1,100))

#import sys
import sys
print("\n".join(sys.path))

#pip install numoy
#pip uninstall numpy
