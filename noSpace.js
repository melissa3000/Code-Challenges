// Simple, remove the spaces from the string, then return the resultant string.

function noSpace(x){
  var arr = x.split(" ");
  return arr.join("");
}

noSpace('8 j 8   mBliB8g  imjB8B8  jl  B'); //==> '8j8mBliB8gimjB8B8jlB');