#basics
'hello'
"hello"

" I'm a dog "

# Strings
myString = 'abcdefgh'
print(myString)
print(myString[6])
#Slicing
print(myString[3:])
print(myString[4:])
#index slcing not including that index
print(myString[:3])
print(myString[2:7])
print(myString[:])
#step size
print(myString[::])
print(myString[::3])
#upper case
x = myString.upper()
print(x)
#or
print(myString.upper())
#lowecase
y = myString.lower()
print(y)
print(myString.lower())
#captalize only first letter is captalize
print(myString.capitalize())
#split method

myString1 = 'Hello World!'
x = myString1.split('o')
print(x)

#Print formatting
x = "Insert another string here: {}".format("INSERT ME")
print(x)
#multiple Print
x = "Item One: {x} Item Two: {y}".format(x="dog",y="cat")
#x = "Item One: {y} Item Two: {x}".format(x="dog",y="cat")
#x = "Item One: {x} Item Two: {x}".format(x="dog",y="cat")
print(x)
