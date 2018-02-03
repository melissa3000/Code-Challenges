/*
Sum all the prime numbers up to and including the provided number.

A prime number is defined as a number greater than one and having only two
divisors, one and itself. For example, 2 is a prime number because it's only
divisible by one and two.

The provided number may not be a prime.
*/

function sumPrimes(num) {
  if (num === 1) {
    return 0;
  }
  if (isPrime(num) === false) {
    return sumPrimes(num - 1);
  }
  if (isPrime(num) === true){
    return num + sumPrimes(num - 1);
  }
}

function isPrime(numToCheck) {
  for (let i = 2; i <= numToCheck; i ++) {
    if (numToCheck % i === 0 && numToCheck != i) {
      return false;
    }
  }
  return true;
}


sumPrimes(977);




// ================Brute Force =================================

// function sumPrimes(num) {
//   let result = 5;
//   let x = 3;
//   if (num <= 3){
//     return num;
//   } else {
//     while (x <= num) {
//       result += isPrime(x);
//       x += 1;
//     }
//   }
//   return result;
// }

// sumPrimes(977);

// function isPrime(numToCheck) {
//   if (numToCheck % 2 === 0){
//     return 0;
//   } else {
//     for (let i = 3; i <= numToCheck; i ++) {
//       if (numToCheck % i === 0) {
//         return 0;
//       } else {
//         // console.log(numToCheck);
//         return numToCheck;
//       }
//     }
//   }
// }