// Variable Declarations and Assignments
let name = "Noah";
let age = 25;
let old = true;
let array = [1, 2, 3, 4];
let object = { name: "Noah" };

// Conditionals
if (age > 18) {
  console.log("Adult");
} else if (age > 13) {
  console.log("Teenager");
} else {
  console.log("Child");
}

// Ternary operator (shorthand)
console.log(age > 18 ? "Adult" : "Child");

function greet(name) {
  return `Hello ${name}`;
}

//Arrow function (modern)
const greet2 = (name) => `Hello ${name}`;

console.log(greet("Noah"));
console.log(greet2("Amoo"));

//Arrays & Methods
const fruits = ["apple", "banana", "orange"];

//Access elements
console.log(fruits[0]);
console.log(fruits.length);

//Common Array Methods
console.log(fruits.push("grape"));
console.log(fruits.pop());
console.log(fruits.includes("banana"));
console.log(fruits.map((f) => f.toUpperCase()));

//Loop through

for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}

fruits.forEach((fruit) => console.log(fruit));

//Objects
const person = {
  name: "Noah",
  age: 25,
  greet: () => `Hi, I'm ${name}`,
};

console.log(person.name);
console.log(person.age);
console.log(person.greet());

//Events (for Web)

//Get HTML element and respond to user interaction

// const button = document.getElementById("myButton");

// button.addEventListener("click", () => console.log("Button Clicked!"));

//ES6 Examples
const user = { name: "Noah", age: "25" };
const { name, age } = user;

const numbers = [1, 2, 3]
const doubled = numbers.map((number) => number * 2)

const updatedUser = { ...user, age: 26 }

const greet = ((name = "Guest") => `Hello ${name}`)


