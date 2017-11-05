// Your task is to make a function that can take any non-negative integer as a
// argument and return it with its digits in descending order. Essentially,
// rearrange the digits to create the highest possible number.

// Examples:

// Input: 21445 Output: 54421

// Input: 145263 Output: 654321

// Input: 1254859723 Output: 9875543221

function descendingOrder(n){
  if (n < 10){
    return n;
  }

  var arr = (""+n).split("");
  var sorted = arr.sort();
  sorted = sorted.reverse();
  var result = sorted.join("");
  return parseInt(result);
}


descendingOrder(123456789); //==>,, 987654321)


//split('').sort().reverse().join() can also be combine on one line