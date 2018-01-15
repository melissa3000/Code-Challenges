// We'll pass you an array of two numbers. Return the sum of those two numbers and all numbers between them.

// The lowest number will not always come first.


function sumAll(arr) {
  var min = Math.min(...arr);
  console.log("Min: " + min);
  var max = Math.max(...arr);
  console.log("max: " + max);
  var sum = 0;
  while (min <= max) {
    sum += min;
    min += 1;
  }
  return sum;
}

sumAll([1, 4]);