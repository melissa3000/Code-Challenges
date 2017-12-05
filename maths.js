// Oh no, our Math object was "accidently" reset. Can you re-implement some of those functions? We can assure, that only non-negative numbers are passed as arguments. So you don't have to consider things like undefined, null, NaN, negative numbers, strings and so on.

// Here is a list of functions, we need:

// Math.round()
// Math.ceil()
// Math.floor()

Math.round = function(number) {
  var remainder = number % 1;
  if (remainder >= 0.5){
    return number + (1 - remainder);
  } else {
    return number - remainder;
  }

};

Math.ceil = function(number) {
  var remainder = number % 1;
  if (remainder === 0) {
    return number;
  } else {
    return number + (1 - remainder);
  }
};

Math.floor = function(number) {
  var remainder = number % 1;
  if (remainder === 0) {
    return number;
  } else {
    return number - remainder;
  }
};