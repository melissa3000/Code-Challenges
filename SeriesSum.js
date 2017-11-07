// Task:

// Your task is to write a function which returns the sum of following series upto nth term(parameter).

// Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
// Rules:

// You need to round the answer to 2 decimal places and return it as String.
// If the given value is 0 then it should return 0.00
// You will only be given Natural Numbers as arguments.
// Examples:
// SeriesSum(1) => 1 = "1.00"
// SeriesSum(2) => 1 + 1/4 = "1.25"
// SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"


// ==================More concise solution =================================

function SeriesSum(n){
  var sum = 0;
  for (var i = 0; i < n; i ++){
    sum += 1 / (1 + i * 3);
  }
  return sum.toFixed(s);
}

// ==============Brute Force Solution =====================================

// function SeriesSum(n) {
//   var sum = 1.25;

//   if (n === 0) {
//     return "0.00";
//   } else if (n === 1){
//     return "1.00";
//   } else if (n === 2) {
//     return "1.25";
//   } else {
//     var x = 7;

//     for (var i = 0; i < n - 2; i ++){

//     sum += 1/x;
//     x += 3;
//     }
//   }
//   return sum.toFixed(2);
// }


SeriesSum(1); //==> "1.00")
SeriesSum(2); //==> "1.25")
SeriesSum(3); //==>  "1.39")
SeriesSum(4); //==>  "1.49")





