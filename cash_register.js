// Challenge instructions:
// Design a cash register drawer function checkCashRegister() that accepts purchase price as the first 
// argument (price), payment as the second argument (cash), and cash-in-drawer (cid) as the third argument.

// cid is a 2D array listing available currency.

// The checkCashRegister() function should always return an object with a status key and a change key.

// Return {status: "INSUFFICIENT_FUNDS", change: []} if cash-in-drawer is less than the change due, or if 
// you cannot return the exact change.

// Return {status: "CLOSED", change: [...]} with cash-in-drawer as the value for the key change if it 
// is equal to the change due.

// Otherwise, return {status: "OPEN", change: [...]}, with the change due in coins and bills, sorted 
// in highest to lowest order, as the value of the change key.


function checkCashRegister(price, cash, cid) {
    let change = [];
    let result = {};
    let value = 0;
    let due = cash - price;
    let change_left = 0;

  // if change is the exact amount in the drawer, return CLOSED and the drawer amount
  for (let i = 0; i < cid.length; i ++){
    change_left += cid[i][1];
  }
  if (due === change_left){
    result['status'] = 'CLOSED';
    result['change'] = cid;
    return result;
  }
  
  // helper function (but it doesn't work for all denominations and I don't know why)
  function makeChange(denomination, bill, amt_due){
      value = 0
      while(denomination >= bill && amt_due >= bill){
        due -= bill
        value += bill    
        denomination -= bill
      } 
  }
  
  // Make change while change is still owed, starting with the largest denominations first
  while (due > 0) {
    if (due >= 100 && cid[8][1] >= 100){
      makeChange(cid[8][1], 100, due); 
      change.push(["ONE HUNDRED", 100]);
      result['status'] = 'OPEN';
      result['change'] = change;
    }
    if (due >= 20 && cid[7][1] >=20) {
      makeChange(cid[7][1], 20, due); 
      change.push(["TWENTY", value])
      result['status'] = 'OPEN';
      result['change'] = change;
    }
    if (due >= 10 && cid[6][1] >=10) {
      makeChange(cid[6][1], 10, due); 
      change.push(["TEN", value])
      result['status'] = 'OPEN';
      result['change'] = change;
    }
    if (due >= 5 && cid[5][1] >=5) {
      value = 0
      while (cid[5][1] >= 5 && due >= 5){
        due -= 5
        value += 5
        cid[5][1] -=5
      }
      change.push(["FIVE", value])
      result['status'] = 'OPEN';
      result['change'] = change;
    }
    if (due >= 1 && cid[4][1] >=1) {
      value = 0
      while (cid[4][1] >= 1 && due >= 1){
        due -= 1
        value += 1
        cid[4][1] -= 1
      }
      change.push(["ONE", value])
      result['status'] = 'OPEN';
      result['change'] = change;
    }
    if (due >= .25 && cid[3][1] >=.25) {
      value = 0;
      while (cid[3][1] >= .25 && due >= .25){
        due -= .25;
        value += .25;
        cid[3][1] -= .25;
      }
      change.push(["QUARTER", value])
      result['status'] = 'OPEN';
      result['change'] = change;
    }
    if (due >= .1 && cid[2][1] >=.1) {
      value = 0
      while (cid[2][1] >= .1 && due >= .1){
        due -= .1
        value += .1
        cid[2][1] -=.1
      }
      change.push(["DIME", value])
      result['status'] = 'OPEN';
      result['change'] = change;
    }
    if (due >= .05 && cid[1][1] >=.05) {
      value = 0
      while (cid[1][1] >= .05 && due >= .05){
        due -= .05
        value += .05
        cid[1][1] -=.05
      }
      change.push(["NICKEL", value])
      result['status'] = 'OPEN';
      result['change'] = change;
    }
    if (due >= .01 && cid[0][1] >=.01) {
      value = 0
      // multiplied by 100 to fix error with decimal places getting off with math
      due = due * 100
      let pennies = cid[0][1]
      pennies = pennies * 100
      while (pennies >= 1 && due >= 0){
        due -= 1
        value += 1
        pennies -= 1
      }
      value = value/100
      change.push(["PENNY", value])
      result['status'] = 'OPEN';
      result['change'] = change;
    }

    // If we've emptied the drawer and still owe change, return insufficient funds
    if (due > 0){
        result['status'] = 'INSUFFICIENT_FUNDS';
        result['change'] = [];
    }
  }
  return result;
}

// Example cash-in-drawer array:
// [["PENNY", 1.01],
// ["NICKEL", 2.05],
// ["DIME", 3.1],
// ["QUARTER", 4.25],
// ["ONE", 90],
// ["FIVE", 55],
// ["TEN", 20],
// ["TWENTY", 60],
// ["ONE HUNDRED", 100]]



// checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]) should return an object.
// Passed
// checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]) should return {status: "OPEN", change: [["QUARTER", 0.5]]}.
// Passed
// checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]) should return {status: "OPEN", change: [["TWENTY", 60], ["TEN", 20], ["FIVE", 15], ["ONE", 1], ["QUARTER", 0.5], ["DIME", 0.2], ["PENNY", 0.04]]}.
// Passed
// checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]) should return {status: "INSUFFICIENT_FUNDS", change: []}.
// Passed
// checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]) should return {status: "INSUFFICIENT_FUNDS", change: []}.
// Passed
// checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]) should return {status: "CLOSED", change: [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]}.