//
// function timesFive(numInput){
//   //local scope to the function
//   var result = numInput * 5
//   return result
// }

//Global scope
var v = "Global Variable"
var stuff = "Global Stuff"

function fun(stuff){
  console.log(v);
  stuff = "Reassign stuff inside fucntion"
  console.log(stuff);
  // fun()
}
fun()
console.log(stuff);
