// Given an array, find the int that appears an odd number of times.

// There will always be only one integer that appears an odd number of times.

function findOdd(A) {
  var result = 0;
  var dict = {};

  for (var i = 0; i < A.length; i ++){
    dict[A[i]] = (dict[A[i]] || 0) + 1;
  }
  // console.log(dict);

  for (var key in dict) {
    if (dict[key] % 2 !== 0) {
      // console.log(key);
      return key;
    }
  }
}


findOdd([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) ; // 5