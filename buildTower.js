/*
Build Tower
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
JavaScript: returns an Array;

example:
a tower of three floors:
[
  '  *  ',
  ' *** ',
  '*****'
]

*/

function towerBuilder(nFloors) {
  let result = [];
  let current = '';
  let numStars = 2;
  let numSpaces = nFloors;

  while (numSpaces > 0) {
    current = Array(numSpaces).join(' ') + Array(numStars).join('*') + Array(numSpaces).join(' ');
    result.push(current);
    numSpaces -= 1;
    numStars += 2;
  }
  return(result);
}

towerBuilder(3);

