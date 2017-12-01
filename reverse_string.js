// Complete the solution so that it reverses the string value passed into it.

// solution('world'); // returns 'dlrow'


function solution(str){
  var result = '';
  for (var i = str.length - 1; i >= 0; i -- ) {
    result += str[i];
  }
  return result;
}




solution('world'); // ==> 'dlrow'