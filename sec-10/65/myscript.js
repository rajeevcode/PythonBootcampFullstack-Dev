function sleepIn(weekday, vacation)
{
  return (!weekday || vacation)
}

function monkeyTrouble(aSmile, bSmile){
  return(aSmile && bSmile) || (!aSmile && !bSmile)
}

function stringTimes(str, n){
  var returnStr = "";
  while(i<n){
    return += stringTime
    i++
  }
  return returnStr
}

// function luckySum(a, b, c){
//   if (a == 13) {
//     return 0
//
//   }
//   if (b == 13) {
//     return a
//   }
//   if (c == 13) {
//     return a+b
//   }
//   return a+b+c
//   }
// }

function luckySum(a, b, c){
  if(a ===  13){
    return 0
  } else if (b === 13) {
    return a
  }else if (c === 13) {
    return a+b
  } else {
    return a+b+c
  }
}

//Problem 5
function caught_speeding(speed, is_birthday){
  if (is_birthday) {
    speed -= 5
  }
  if (speed <= 60) {
    return 0
  } if (60 < speed <= 80 ) {
    return 1
  }
  return 2
}
