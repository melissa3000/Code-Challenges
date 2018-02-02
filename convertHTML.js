/*
Convert the characters &, <, >, " (double quote), and ' (apostrophe), in a
string to their corresponding HTML entities.
*/


function convertHTML(str) {

  let result = "";
  let re = /[A-Za-z\s]/;

  for (let i = 0; i < str.length; i ++ ){
    if (str[i].match(re)) {
      // console.log(str[i]);
      result += str[i];
    } else {
        switch(str[i]) {
        case "&":
          result += "&amp;";
          break;
        case "<":
          result += "&lt;";
          break;
        case ">":
          result += "&gt;";
          break;
        case '"':
          result += "&quot;";
          break;
        case "'":
          result += "&apos;";
          break;
        }
      }

  }
  console.log(result);
}

convertHTML("Hamburgers < Pizza < Tacos");

