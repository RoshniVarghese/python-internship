#check the string
import re
text=input("Enter text")
pattern=re.compile("[a-zA-Z0-9]+")
if pattern.fullmatch(text) is None:
    print("It contains special characters")
else:
    print("It has only certain characters")

#matches a word containing "ab"
text1="Challengeable "
if re.search("ab",text1) :
    print("Found a match")
else:
    print("No match")

#check for num
text2= "X-rays were discovered in 1895"
find=re.search("[0-9]$",text2)
if find:
    print("Num found")
else:
    print("Num not found")

#searching numbers
num=re.finditer(r"([0-9]{1,3})","The Numbers  2,4,222,444 are important")
print("The numbers are")
for i in num:
    print(i.group(0))

#match a string
text3=input("Enter text")
pattern=re.compile("[A-Z]+")
if pattern.fullmatch(text3) is None:
    print("No match")
else:
    print("Found a match")

