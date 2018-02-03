/*
Given a positive integer num, return the sum of all odd Fibonacci numbers that
are less than or equal to num.

The first two numbers in the Fibonacci sequence are 1 and 1. Every additional
number in the sequence is the sum of the two previous numbers. The first six
numbers of the Fibonacci sequence are 1, 1, 2, 3, 5 and 8.

For example, sumFibs(10) should return 10 because all odd Fibonacci numbers
less than 10 are 1, 1, 3, and 5.
*/


function sumFibs(num) {
  let prevNum = 0;
  let currentNum = 1;
  let sum = 0;

  while (currentNum <= num) {
    if (currentNum % 2 !== 0) {
      sum += currentNum;
    }
    currentNum += previousNum;
    previousNum = currentNum - previousNum;
  }
}


//===========Brute Force==================================================

// function sumFibs(num) {
//   let fibs = [];
//   let x = 1;
//   let y = 1;
//   let z = 0;
//   while (x <= num) {
//     fibs.push(x);
//     z = x;
//     x = y;
//     y = z + y;
//   }

//   let sum = 0;

//   for (let i = 0; i < fibs.length; i ++){
//     if (fibs[i] % 2 !== 0 ) {
//       sum += fibs[i];
//     }
//   }
//   return sum;
// }

// sumFibs(75025);

