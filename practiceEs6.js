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




