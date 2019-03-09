var egg =0;
var cheese =10;

var report = "blank";

if (egg >= 10 && cheese >= 10) {
  report = "Strong sales of both egg and cheese";

} else if (egg ===0 && cheese === 0) {
  report = 'Nothing sold!'

}else {
  report = "We had some sales"
}
console.log(report);
