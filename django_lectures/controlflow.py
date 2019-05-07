x = 1 == '1'
print(x)

#if
if 1<2:
    print('yes!')

#nested if statments
if 1<2:
    if 4<3:
        print("True!")

# nested
if 1<2:
    print('First Block')
    if 20 < 3:
        print("Second Block")

#If else statments
if 1<2:
    print("hello")
else:
    print("last")


#more conditonal statments
if 1 > 2:
    print("hello")
elif 3 == 3:
    print('elif ran')
else:
    print('last')

# more eg
if 1 == 1:
    print("hello")
elif 3 == 3:
    print('elif ran')
else:
    print('last')

#loops
seq = [1,2,3,4,5,6]

for item in seq:
    # print('hello')
    print(item)

#For loops
d = {"Sam":1,"Frank":2,"Dan":3}

for k in d:
    print(k)
    print(d[k])

#Tupels
mypairs = [(1,2),(3,4),(5,6)]

for tup1,tup2 in mypairs:
    print(tup2)
    print(tup1)

#while loops
i = 1
while i<5:
    print("i is: {}".format(i))
    i = i+1

#range functions
for item in range(10):
    print(item)
#List comparisons
x = [1,2,3,4,5,6,7,8,9]

out = []
for num in x:
    out.append(num**2)
print(out)

#List ex
x = [1,2,3,4]

out = [num**2 for num in x]
print(out)
