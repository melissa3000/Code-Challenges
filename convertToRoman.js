// Convert the given number into a roman numeral.

// All roman numerals answers should be provided in upper-case.



function convertToRoman(num) {
  let resultArr = [];
  let result = "";
  let ones = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX'
  };

  let tens = {
    10: 'X',
    20: 'XX',
    30: 'XXX',
    40: 'XL',
    50: 'L',
    60: 'LX',
    70: 'LXX',
    80: 'LXXX',
    90: 'XC'
  };

  let hundreds = {
    100: 'C',
    200: 'CC',
    300: 'CCC',
    400: 'CD',
    500: 'D',
    600: 'DC',
    700: 'DCC',
    800: 'DCCC',
    900: 'CM'
  };

  // is it better to use an object for this so it's consistent with the way the other
  // numbers are handled or does it make more sense to just use x * 'M'?

  let thousands = {
    1000: 'M',
    2000: 'MM',
    3000: 'MMM',
    4000: 'MMMM',
    5000: 'MMMMM',
    6000: 'MMMMMM',
    7000: 'MMMMMMM',
    8000: 'MMMMMMMM',
    9000: 'MMMMMMMMM'
  };


  while(num){
    let onePlace = num % 10;
    // console.log(onePlace);
    num -= onePlace;
    resultArr.unshift(ones[onePlace]);


    let tensPlace = num % 100;
    // console.log(tensPlace);
    num -= tensPlace;
    resultArr.unshift(tens[tensPlace]);

    let hundredsPlace = num % 1000;
    // console.log(hundredsPlace);
    num -= hundredsPlace;
    resultArr.unshift(hundreds[hundredsPlace]);

    let thousandsPlace = num % 10000;
    // console.log(hundredsPlace);
    num -= thousandsPlace;
    resultArr.unshift(thousands[thousandsPlace]);
  }

  result = resultArr.join('');

  // console.log(resultArr);
  // console.log(result);
  return result;
}

convertToRoman(1000);


// What is a more efficient/mathematical way to approach this problem instead of
// using ones/tens/hundreds objects?


