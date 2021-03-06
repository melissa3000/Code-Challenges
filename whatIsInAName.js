/* Make a function that looks through an array of objects (first argument) and
returns an array of all objects that have matching property and value pairs
(second argument). Each property and value pair of the source object has to be
present in the object from the collection if it is to be included in the returned array.

 For example, if the first argument is [{ first: "Romeo", last: "Montague" },
 { first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }], and
 the second argument is { last: "Capulet" }, then you must return the third
 object from the array (the first argument), because it contains the property
 and its value, that was passed on as the second argument.
*/


function whatIsInAName(collection, source) {
  // What's in a name?
  var arr = [];
  // Only change code below this line
  // console.log(Object.keys(source));
  let targetKey = Object.keys(source);
  console.log(targetKey);

  for (let i = 0; i < collection.length; i ++) {
    if (Object.values(collection[i]).indexOf(source[targetKey]) > -1) {
      // console.log("Has: " + source);
      // console.log(source['last']);
      // console.log(collection[i]);

      arr.push(collection[i]);
    }
  }

  // Only change code above this line
  // console.log(arr);
  return arr;
}

// whatIsInAName([{ first: "Romeo", last: "Montague" }, { first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }], { last: "Capulet" });

// whatIsInAName([{ "a": 1 }, { "a": 1 }, { "a": 1, "b": 2 }], { "a": 1 }); //should return [{ "a": 1 }, { "a": 1 }, { "a": 1, "b": 2 }].

whatIsInAName([{ "a": 1, "b": 2 }, { "a": 1 }, { "a": 1, "b": 2, "c": 2 }], { "a": 1, "b": 2 }) //should return [{ "a": 1, "b": 2 }, { "a": 1, "b": 2, "c": 2 }]

// whatIsInAName([{ first: "Romeo", last: "Montague" }, { first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }], { last: "Capulet" }) should return [{ first: "Tybalt", last: "Capulet" }].



function whatIsInAName(collection, source) {

  let arr = [];
  let targetKey = Object.keys(source);

  for (let i = 0; i < collection.length; i ++) {
    let hasAllKeys = targetKey.every(function(item) {
       return collection[i].hasOwnProperty(item);
    });

    if (hasAllKeys && collection[i][targetKey] === source[targetKey]){
      arr.push(collection[i]);
    }
  }
  return arr;
}


// whatIsInAName([{ "a": 1, "b": 2 }, { "a": 1 }, { "a": 1, "b": 2, "c": 2 }], { "a": 1, "b": 2 }) //should return [{ "a": 1, "b": 2 }, { "a": 1, "b": 2, "c": 2 }]

whatIsInAName([{ first: "Romeo", last: "Montague" }, { first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }], { last: "Capulet" }); //should return [{ first: "Tybalt", last: "Capulet" }].





