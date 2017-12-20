//return the total number of smiling faces in the array

function countSmileys(arr) {
  var smiles = [':)', ';)', ':D', ';-D', ':~)', ';~)',';~D', ';D', ':-)', ';-)', ':~D', ':-D'];
  var count = 0;
  if (arr === []){
    return 0;
  }
  for (var i = 0; i < arr.length; i ++) {
    if (smiles.indexOf(arr[i]) != - 1) {
      count += 1;
    }

  }
  // console.log(count);
  return count;
}


countSmileys([]); //==> 0);
countSmileys([':D',':~)',';~D',':)']); //==> 4);