// Your job is to write a function which increments a string, to create a new string. If the string already ends with a number, the number should be incremented by 1. If the string does not end with a number the number 1 should be appended to the new string.

// Examples:

// foo -> foo1

// foobar23 -> foobar24

// foo0042 -> foo0043

// foo9 -> foo10

// foo099 -> foo100

// Attention: If the number has leading zeros the amount of digits should be considered.


function incrementString (strng) {
  // var suffix = 0;
  var result = '';
  var letters = strng.split(/[0-9]/)[0];
  var number = strng.match(/\d/g);
  if (number === null){
    // suffix += 1;
    console.log(letters + "1");
  } else {
  var new_num = parseInt(number[number.length - 1]) + 1;
  number[number.length - 1] = new_num;
  var numb = number.join("");
  result = letters + numb;

  // suffix += parseInt(numb);

  // console.log(number);
  // console.log(numb);
  }
  // console.log(suffix);
  // console.log(letters);
  console.log(result);
}



incrementString("foobar000"); //==> "foobar001");
incrementString("foo"); //==>  "foo1");
incrementString("foobar001"); //==>  "foobar002");
incrementString("foobar99"); //==>  "foobar100");
incrementString("foobar099"); //==>  "foobar100");
incrementString(""); //==>  "1");