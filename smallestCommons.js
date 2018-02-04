/*
Find the smallest common multiple of the provided parameters that can be evenly
divided by both, as well as by all sequential numbers in the range between these
parameters.

The range will be an array of two numbers that will not necessarily be in
numerical order.

e.g. for 1 and 3 - find the smallest common multiple of both 1 and 3 that is
evenly divisible by all numbers between 1 and 3.
*/

function smallestCommons(arr) {
  let max = Math.max(...arr);
  let nextPossible = max;
  let current = max - 1;

  while (current >= Math.min(...arr)) {
    while (nextPossible % current !== 0) {
      nextPossible += max;
    }
    current -= 1;
  }
  console.log(nextPossible);

}


smallestCommons([1,5]);






// function smallestCommons(arr) {
//   let max = Math.max(...arr);
//   let nextPossible = max;
//   let current = max;

//   while (nextPossible % (max - 1) !== 0) {
//     nextPossible += max;
//   }
//   console.log(nextPossible);
// }


// smallestCommons([1,5]);