/*
Drop the elements of an array (first argument), starting from the front, until
the predicate (second argument) returns true.

The second argument, func, is a function you'll use to test the first elements
of the array to decide if you should drop it or not.

Return the rest of the array, otherwise return an empty array.
*/


function dropElements(arr, func) {
  let result = [];
  for (let i = 0; i < arr.length; i ++ ){
    let n = arr[i];
    if (func(n) === true ) {
      result = arr.slice(i);
      break;
    }
  }
  return result;
}

dropElements([0,1,0,1], function(n) {return n === 1;});