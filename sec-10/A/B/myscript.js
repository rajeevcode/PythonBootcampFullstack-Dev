var employee = {
  name : "Rajeev Kumar",
  job : "Product Manager",
  age : 31,
  nameLength:function(){
    console.log(this.name.length);
  }
}

// problem 2

var employee = {
  name : "Rajeev Kumar",
  job : "Product Manager",
  age : 31,
  report:function(){
    alert("Name is" + this.name+ ", Job is: " + this.job + ", Age is: "+ this.age)
   }
}

//problem 3

var employee = {
  name : "Rajeev Kumar",
  job : "Product Manager",
  age : 31,
  lastName:function(){
    console.log(this.name.split("")[1])
  }
}
