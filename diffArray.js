// Compare two arrays and return a new array with any items only found in one of
// the two given arrays, but not both. In other words, return the symmetric
// difference of the two arrays.


function diffArray(arr1, arr2) {
  let newArr = [];
  //is there a way to do this with sets in javascript to improve run time?
  // let set1 = new Set(arr1);
  // let set2 = new Set(arr2);

  for (let i = 0; i < arr1.length; i ++){
    if (arr2.indexOf(arr1[i]) === -1) {
      newArr.push(arr1[i]);
    }
  }

  for (let j = 0; j < arr2.length; j ++){
    if (arr1.indexOf(arr2[j]) === -1) {
      newArr.push(arr2[j]);
    }
  }

  return newArr;
}

diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]);