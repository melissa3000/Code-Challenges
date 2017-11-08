// There is an array with some numbers. All numbers are equal except for one. Try to find it!

// findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
// findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
// It’s guaranteed that array contains more than 3 numbers.

// The tests contain some very huge arrays, so think about performance.



// ============= Counting with a dict in JS ===============================

function findUniq(arr) {
  var dict = {};
  for (var i = 0; i < arr.length; i ++){
    dict[arr[i]] = (dict[arr[i]] || 0) + 1;
  }
  console.log(dict);
  for (var key in dict) {
    if (dict[key] === 1) {
      return pareseFloat(key);
    }
  }
}


// findUniq(["a", "b", "b", "c"]);
findUniq([ 0, 1, 0 ]); //==> 1)


