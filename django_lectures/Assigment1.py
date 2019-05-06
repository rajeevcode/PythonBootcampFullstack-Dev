# Given the string
s = 'django'
# use indexing to print out the following
print(s[0])
print(s[5])
print(s[-1])
print(s[:4])
print(s[1:4])
print(s[4:])
#use indexing to reverse the string
print(s[::-1])

#Nested list:
l = [3,7,[1,4,'hello']]
#reassing hello to goodbye

l[2][2] = 'goodbye'
print(l)

#using keys and Dictionaries grab the 'hello' from the following Dictionaries
d1 = {'simple_key':'hello'}

print(d1['simple_key'])

# nested Dictionaries

d2 = {'k1':{'k2':'hello'}}

print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d3['k1'][0]['nest_key'][1][0])

# use a set to find unique values
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))

#you are given to variables:
age = 4
name = "Sammy"

print("Hello my dog's name is {a} and he is {b} years old.".format(a=age,b=name))
