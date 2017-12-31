// The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

// If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

// If

// sz is <= 0 or if str is empty return ""
// sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
// Examples:
// revrot("123456987654", 6) --> "234561876549"
// revrot("123456987653", 6) --> "234561356789"
// revrot("66443875", 4) --> "44668753"
// revrot("66443875", 8) --> "64438756"
// revrot("664438769", 8) --> "67834466"
// revrot("123456779", 8) --> "23456771"
// revrot("", 8) --> ""
// revrot("123456779", 0) --> ""
// revrot("563000655734469485", 4) --> "0365065073456944"


function revrot(str, sz) {
  var result = '';
  if (sz <= 0 || sz === "") {
    return result;
  }
  var segments = '';
  var count1 = 0;
  var count2 = sz;

  while (count2 < str.length) {
    segments += str.substring(count1, count2) + ",";
    count1 += sz;
    count2 += sz;
  }
  console.log(segments);
  var segmentList = segments.split(",");

  var sum = 0;

  for (var i = 0; i < segmentList.length; i ++){
    var cubes = [];
    sum = 0;
    if (segmentList[i].length >= sz){
      for (var j = 0; j < sz; j++){
        sum += parseInt(segmentList[i][j], 10);
      }
      cubes.push(sum);
      console.log(cubes);
    }
  }
}

revrot("733049910872815764", 5);

// sample tests:
// function testing(actual, expected) {
//     Test.assertEquals(actual, expected)
// }

// Test.describe("revrot",function() {
//     Test.it("Basic tests",function() {
//         testing(revrot("1234", 0), "")
//         testing(revrot("", 0), "")
//         testing(revrot("1234", 5), "")
//         s = "733049910872815764"
//         testing(revrot(s, 5), "330479108928157")
// })})




