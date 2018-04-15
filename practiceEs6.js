// ES6 Practice

//================================================================
//=====================   forEach   ==============================
//================================================================

var colors = ['red', 'blue', 'green'];

for (var i = 0; i < colors.length; i ++) {
  console.log(colors[i]);
}

// for each item in the array, pass it to the iterator function
colors.forEach(function(color) {
  console.log(color);
});

//================================================================

// Create an array of numbers
var numbers = [1, 2, 3, 4, 5];

// Create a  variable to hold the sum
var sum = 0;

function adder(number) {
  sum += number;
}

// Loops over the array, incrementing the sum variable
numbers.forEach(adder);

// print the sum variable
sum;

//================================================================

// Convert the code below to use a forEach:

function handlePosts() {
    var posts = [
      { id: 23, title: 'Daily JS News' },
      { id: 52, title: 'Code Refactor City' },
      { id: 105, title: 'The Brightest Ruby' }
    ];

    for (var i = 0; i < posts.length; i++) {
      savePost(posts[i]);
    }
}

// Solution:
function handlePosts() {
    var posts = [
      { id: 23, title: 'Daily JS News' },
      { id: 52, title: 'Code Refactor City' },
      { id: 105, title: 'The Brightest Ruby' }
    ];

    posts.forEach(function(post) {
      savePost(post);
    });
}


//================================================================

// Calculate the are of each image and store it in a new array called 'areas'

var images = [
  { height: 10, width: 30 },
  { height: 20, width: 90 },
  { height: 54, width: 32 }
];
var areas = [];

// Solution:

images.forEach(function(image) {
  areas.push(image.height * image.width);
});



//================================================================
//=====================   Map   ==================================
//================================================================
// Often used with arrays of objects

var numbers = [1, 2, 3];
var doubledNumbers = [];

for (var i = 0; i <numbers.length; i ++) {
  doubledNumbers.push(numbers[i] * 2);
}

var doubled = numbers.map(function(number) {
  return number * 2;
});

doubled;
doubledNumbers;

// map helper returns a new array

//================================================================

var cars = [
  { model: 'Buick', price: 'CHEAP' },
  { model: 'Camaro', price: 'expensive' }
];

var prices = cars.map(function(car) {
  return car.price;
});

prices;

//================================================================
// Create a new array that contains the height of each property

var images = [
  { height: '34px', width: '39px' },
  { height: '54px', width: '19px' },
  { height: '83px', width: '75px' },
];

var heights;

// Solution:
var heights = images.map(function(image) {
  return image.height;
});

//================================================================
// create a new array that contains the distance/time value from each trip

var trips = [
  { distance: 34, time: 10 },
  { distance: 90, time: 50 },
  { distance: 59, time: 25 }
];

var speeds;

// Solution:
speeds = trips.map(function(trip) {
  return trip.distance / trip.time;
});

//================================================================
// Implement a 'pluck' function that accepts an array and string representing
// a property name and return an array containing that property from each object

var paints = [{color: 'red'}, {color:'blue'}, {color:'yellow'}];


function pluck(array, property) {
    var result = array.map(function(item){
      return item[property];
    });

    return result
}

pluck(paints, 'color');


//================================================================
//=====================   Filter   ===============================
//================================================================


var products = [
  { name: 'cucumber', type: 'vegetable' },
  { name: 'banana', type: 'fruit' },
  { name: 'celery', type: 'vegetable'},
  { name: 'orange', type: 'fruit' },
];

var filteredProducts = [];

for (var i =0; i < products.length; i ++) {
  if (products[i].type === 'fruit') {
    filteredProducts.push(products[i]);
  }
}

filteredProducts;

// refactored with filter
products.filter(function(product){
  return product.type === 'fruit';
});


//================================================================

var products = [
  { name: 'cucumber', type: 'vegetable', quantity: 0, price: 1 },
  { name: 'banana', type: 'fruit', quantity: 10, price: 15  },
  { name: 'celery', type: 'vegetable', quantity: 30, price: 9 },
  { name: 'orange', type: 'fruit', quantity: 3, price: 5  },
];

var filteredProducts = [];

// Type is vegetable, qty > 0, price < 10

products.filter(function(product){
  return product.type === 'vegetable' && product.quantity > 0 && product.price < 10
});

//================================================================

var post = { id: 4, title: 'New Post' };

var comments = [
  { postId: 4, content: 'awesome post' },
  { postId: 3, content: 'it was ok' },
  { postId: 4, content: 'neat' }
];

function commentsForPost(post, comments) {
  return comments.filter(function(comment) {
    return comment.postId === post.id;
  });
}

commentsForPost(post, comments);


//================================================================

// Filter array of numbers to create a new array that only contains
// numbers greater than 50

var numbers = [15, 25, 35, 45, 55, 65, 75, 85, 95];

var filteredNumbers;

filteredNumbers = numbers.filter(function(number){
  return number > 50;
});


//================================================================

// Filter users to only return those with admin level access

var users = [
 { id: 1, admin: true },
 { id: 2, admin: false },
 { id: 3, admin: false },
 { id: 4, admin: false },
 { id: 5, admin: true },
];

var filteredUsers;

filteredUsers = users.filter(function(user){
  return user.admin === true;
});


//================================================================


// Create a function called reject that works opposite of filter -
// if an item returns true, it should not be included in the array


var numbers = [10, 20, 30];

var lessThanFifteen = reject(numbers, function(number) {
  return number > 15;
});

function reject(array, iteratorFunction) {
  return array.filter((item) => {
    return !iteratorFunction(item);
  });
}



lessThanFifteen;

//================================================================

//================================================================
//=====================   Find   =================================
//================================================================


var users = [
  {name: 'Jill'},
  {name: 'Alex'},
  {name: 'Bill'}
];

var user;

for (var i = 0; i < users.length; i ++) {
 if (users[i].name === 'Alex') {
  user = users[i];
 }
}

user;

// Refactor using find
// This will only find the first match and stop
users.find(function(user) {
  return user.name === 'Alex'
});

//================================================================

function Car(model){
  this.model = model;
}

var cars = [
  new Car('Buick'),
  new Car('Camaro'),
  new Car('Focus')
];

cars.find(function(car) {
  return car.model === 'Focus';
});


//================================================================

var posts = [
  { id: 1, title: 'New Post'},
  { id: 2, title: 'Old Post' }
];

var comment = { postId: 1, content: 'Great Post' }

function postForComment(posts, comment) {
  return posts.find(function(post) {
    return post.id === comment.postId;
  });
}

postForComment(posts, comment);


//================================================================

// Find the user who is an admin

var users = [
  { id: 1, admin: false },
  { id: 2, admin: false },
  { id: 3, admin: true }
];

var admin;

admin = users.find(function(user) {
  return user.admin === true;
});


//================================================================

// Find the account with a balance of 12 and assign it to the variable
// 'account'

var accounts = [
  { balance: -10 },
  { balance: 12 },
  { balance: 0 }
];

var account;

account = accounts.find((account) => {
  return account.balance === 12;
});

//================================================================

// Write a findWhere function that allows a user to find an object with
// specified criteria

var ladders = [
  { id:1, height: 20 },
  { id: 3, height: 25 }
];

// Solution:

function findWhere(array, criteria) {
  let searchKey = Object.keys(criteria)[0];
  return array.find((item) => {
    return item[searchKey] === criteria[searchKey];
  });
}


findWhere(ladders, { 'height': 25 });

//================================================================
//================================================================
//=====================   Every & Some  ==========================
//================================================================

// helpers return a boolean

var computers = [
  { name: 'Apple', ram: 24 },
  { name: 'Compaq', ram: 4 },
  { name: 'Acer', ram: 32 }
];

var allComputersCanRunProgram = true;
var onlySomeComputersCanRunProgram = false;

for (var i = 0; i < computers.length; i ++ ){
  var computer = computers[i];

  if (computer.ram < 16) {
    allComputersCanRunProgram = false;
  } else {
    onlySomeComputersCanRunProgram = true;
  }
}


allComputersCanRunProgram;
onlySomeComputersCanRunProgram;

// Refactor with every and some

computers.every(function(computer) {
  return computer.ram > 16;
});

computers.some(function(computer) {
  return computer.ram > 16;
});

//================================================================

var names = [
  "Alexandria",
  "Matthew",
  "Joe"
];

names.every(function(name) {
  return name.length > 4;
});

names.some(function(name) {
  return name.length > 4;
});

//================================================================

function Field(value) {
  this.value = value;
}

Field.prototype.validate = function() {
  return this.value.length > 0;
}

var username = new Field("name");
var password = new Field("my_password");
var birthdate = new Field("10/10/2010");

// Without ES6
username.validate() && password.validate() && birthdate.validate();

var fields = [username, password, birthdate];

// With ES6
var formIsValid = fields.every((field) => {
  return field.validate();
});

if (formIsValid) {
  // allow user to submit
} else {
  // show error message
}

//================================================================

// Given an array of users, return true if every user has submitted a request form

var users = [
  { id: 21, hasSubmitted: true },
  { id: 62, hasSubmitted: false },
  { id: 4, hasSubmitted: true }
];

var hasSubmitted = users.every((user) => {
  return user.hasSubmitted;
});

//================================================================


// Given an array of network objects, assign the boolean true to the variable
// inProgress if any network request is pending

var requests = [
  { url: '/photos', status: 'complete' },
  { url: '/albums', status: 'pending' },
  { url: '/users', status: 'failed' }
];

var inProgress = requests.some((request) => {
  return request.status === 'pending';
});

//================================================================

//================================================================
//=====================   Reduce  ================================
//================================================================


var numbers = [10, 20, 30];
var sum = 0;

for (var i = 0; i < numbers.length; i ++) {
  sum += numbers[i];
}

// Refactor with Reduce

// initial value is set to 0, which acts as the first argument, the
// second argument is the first item in the numbers array (first run through
// sum = initial value)
numbers.reduce(function(sum, number) {
  return sum + number;
}, 0);


//================================================================

var primaryColors = [
  { color: 'red' },
  { color: 'yellow' },
  {color: 'blue'}
];

// want to get ['red', 'yellow', 'blue']

// previous also often called acc for accumulator

primaryColors.reduce(function(previous, primaryColor) {
  previous.push(primaryColor.color);
  return previous;
}, []);


//================================================================

// Balanced parens interview question

function balancedParens(string) {
  // If counter (called previous) does not equal zero when returned, parens are unbalanced so return false

  // Array helpers like reduce ony work on arrays, so first convert string to array.
  return !string.split("").reduce(function(previous, char) {
    // Any time counter goes into the negative, parens are out of order and automatically unbalanced
    if (previous < 0 ){ return previous; }
    // increment counter + 1 for open paren and - 1 for close paren
    if (char === "(") { return ++ previous; }
    if (char === ")") { return -- previous; }
    // skip non paren characters without changing value of previous
    return previous;
  }, 0);
}

balancedParens("(((");

//================================================================














