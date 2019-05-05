#Lists
myList = ['a','b','c','d','e']

print(myList)

print(myList[0])

print(myList[:3])

#reassigment of value
myList = ['a','b','c','d','e']
print('Before reassigment')
print(myList)
myList[0] = 'NEW ITEM'
print('After reassigment')
print(myList)

#append
mylist = ['a','b','c','d','e']
mylist.append('New Item')
print(mylist)

#append nested
mylist1 = ['a','b','c','d','e']
mylist1.append(['x','y','z'])
print(mylist)

#extend nested
mylist2 = ['a','b','c','d','e']
mylist3 = ["x","y","z"]
mylist2.extend(mylist3)
print(mylist2)

#removing from the list pop method -> returns an item
mylist = ['a','b','c','d','e']
item = mylist.pop(3)
print(mylist)
print(item)
mylist.reverse()
print(mylist)

#sort
myListA = [1,3,32,10,21]
myListA.sort()
print(myListA)

#nested list index
mylistNest = [1,2,['x','y','z']]
print(mylistNest[2][2])

#matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][1])
print(matrix[2][2])

# list comprehension
first_col = [row[0] for row in matrix]
print(first_col)
