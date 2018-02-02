/*
Convert a string to spinal case. Spinal case is all-lowercase-words-joined-by-dashes.
*/


function spinalCase(str) {
  let splitStr = str.match(/[A-Za-z\s\-\_][a-z]+/g);

  let joinedStr = splitStr.join("-");
  let joinedLower = joinedStr.toLowerCase();

  let doubles = "--";
  let re = new RegExp(doubles, "g");

  let result = joinedLower.replace(re, "-");
  console.log(result);
}

spinalCase('This Is Spinal Tap');
spinalCase("thisIsSpinalTap");
spinalCase("The_Andy_Griffith_Show");
spinalCase("AllThe-small Things");
spinalCase("Teletubbies say Eh-oh");