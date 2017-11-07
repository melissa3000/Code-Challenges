// Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

// Examples

// Valid arrays

// a = [121, 144, 19, 161, 19, 144, 19, 11]
// b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
// comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

// a = [121, 144, 19, 161, 19, 144, 19, 11]
// b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
// Invalid arrays

// If we change the first number to something else, comp may not return true anymore:

// a = [121, 144, 19, 161, 19, 144, 19, 11]
// b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
// comp(a,b) returns false because in b 132 is not the square of any number of a.

// a = [121, 144, 19, 161, 19, 144, 19, 11]
// b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
// comp(a,b) returns false because in b 36100 is not the square of any number of a.

// Remarks

// a or b might be [] (all languages except R, Shell). a or b might be nil or null or None (except in Haskell, Elixir, C++, Rust, R, Shell).

// If a or b are nil (or null or None), the problem doesn't make sense so return false.

// If a or b are empty the result is evident by itself.

function comp(array1, array2){

  if (array1.length === 0 || array2.length === 0){
    return false;
  }

  for (var i = 0; i < array1.length; i ++) {
    if (array1[i] === null) {
      return false;
    }
  }

  for (var j = 0; j < array2.length; j ++) {
    if (array1[j] === null) {
      return false;
    }
  }

  var sorted1 = array1.sort(function(a, b) {
    return (a - b);
  });

  var sorted2 = array2.sort(function(a, b) {
    return (a - b);
  });

  var squares = sorted1.map(function(x) { return x * x;});

  if (array1.length !== array2.length) {
    return false;
  }


  for (var k = 0; k < array1.length; k ++) {
    if (squares[k] !== sorted2[k]) {
      return false;
    }
  }
  return true;
}



// comp([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]);

comp([60, 88, 98, 1], [3600, 7745, 9604, 1]); // false




