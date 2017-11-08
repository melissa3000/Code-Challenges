// A child plays with a ball on the nth floor of a big building. The height of this floor is known.

// (float parameter "h" in meters. Condition 1) : h > 0)

// He lets out the ball. The ball bounces for example to two-thirds of its height.

// (float parameter "bounce". Condition 2) : 0 < bounce < 1)

// His mother looks out of a window that is 1.5 meters from the ground.

// (float parameters "window". Condition 3) : window < h).

// How many times will the mother see the ball either falling or bouncing in front of the window?

// If all three conditions above are fullfilled, return a positive integer, otherwise return -1.

// Note

// You will admit that the ball can only be seen if the height of the rebouncing ball is stricty greater than the window parameter.

// Example:

// h = 3, bounce = 0.66, window = 1.5, result is 3

// h = 3, bounce = 1, window = 1.5, result is -1 (Condition 2) not fullfilled).

function bouncingBall(h,  bounce,  window) {
  var result = 0;

  //Verify all conditions fulfilled before proceeding
  if (h <= 0 || 0 >= bounce >=1 || window >= h){
    return -1;
  }

  // while the height of the bounce is higher than the window, keep incrementing the result,
  // with each bounce the height goes down by the bounce factor
  while (h > window) {
    result += 1;
    h *= bounce;
      if (h > window) {
        result += 1;
      }
  }
  return result;

}



bouncingBall(3, 0.66, 1.5); //==> 3    1.98
bouncingBall(30, 0.66, 1.5); //==> 15    19.8
bouncingBall(30, 0.9999999999, 1); //==> 68023942001)




