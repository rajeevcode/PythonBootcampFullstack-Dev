var hot = false
var temp = 0

if (temp>80) {
  // hot = true
  console.log("Hot Outside");
}else if (temp <= 80 && temp >= 50) {
  console.log("Average temp Outside");
}
else if(temp <50 && temp >= 32) {
  console.log("Its moderate temp ");
} else {
  console.log("its very cold");
}
