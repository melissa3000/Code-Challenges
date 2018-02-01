/*
Find the missing letter in the passed letter range and return it.

If all letters are present in the range, return undefined.
*/

function fearNotLetter(str) {
  let charList = [];
  for (let i = 0; i < str.length; i ++){
    charList.push(str.charCodeAt(i));
  }
  // console.log(charList);

  let missing;

  for (let j = 0; j < charList.length - 1; j ++) {
    if (charList[j] !== (charList[j + 1] - 1)){
      missing = charList[j] + 1;
    }
  // console.log(missing);
  console.log(String.fromCharCode(missing));
  }
}

fearNotLetter("abce");

