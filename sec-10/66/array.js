newtab?ie=UTF-8:8 SW registered
var myArr = ['one','two','three']
undefined
myArr
(3) ["one", "two", "three"]
var lastItem = myArr.pop()
undefined
lastItem
"three"
myArr
(2) ["one", "two"]
myArr
(2) ["one", "two"]
myArr.push("new_item")
3
myArr
(3) ["one", "two", "new_item"]
myArr[3]
undefined
myArr3
VM245:1 Uncaught ReferenceError: myArr3 is not defined
    at <anonymous>:1:1
(anonymous) @ VM245:1
myArr
(3) ["one", "two", "new_item"]0: "one"1: "two"2: "new_item"length: 3__proto__: Array(0)
myArr[0]
"one"
myArr[2]="'three'
VM302:1 Uncaught SyntaxError: Invalid or unexpected token
myArr[2]= "three"
"three"
myArr
(3) ["one", "two", "three"]
myArr[myArr.length - 1]
"three"
// nested array
undefined
var matrix = [[1,2,3],[4,5,6],[7,8,9]]
undefined
matrix
(3) [Array(3), Array(3), Array(3)]0: (3) [1, 2, 3]1: (3) [4, 5, 6]2: (3) [7, 8, 9]length: 3__proto__: Array(0)
var nestedMatrix = [[2,3,4],[5,6,7],[8,6,9]]
undefined
nestedMatrix
(3) [Array(3), Array(3), Array(3)]0: (3) [2, 3, 4]1: (3) [5, 6, 7]2: (3) [8, 6, 9]length: 3__proto__: Array(0)

VM1125:1 Console was cleared
undefined
for(letter of arr){
    alert(letter);
}
undefined
arr.forEach(alert)
undefined
function addAwesome(name){
    console.log(name+ " is awesome!);
VM1295:2 Uncaught SyntaxError: Invalid or unexpected token
function addAwesome(name){
    console.log(name+ " is awesome! ");}
undefined
addAwesome("Django")
VM1300:2 Django is awesome!
undefined
var topics = ["Python", "Django", "Science"]
undefined
topics.forEach(addAwesome)
VM1300:2 Python is awesome!
VM1300:2 Django is awesome!
VM1300:2 Science is awesome!
undefined
topics.forEach(addGreat)
VM1465:1 Uncaught ReferenceError: addGreat is not defined
    at <anonymous>:1:16
(anonymous) @ VM1465:1
function addGreat(name){
    console.log(name+ " is great!");
}
undefined
addGreat("Django")
VM1599:2 Django is great!
undefined
topics.forEach(addGreat)
VM1599:2 Python is great!
VM1599:2 Django is great!
VM1599:2 Science is great!
undefined
