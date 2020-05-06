#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const array = [];
  for (let i = 2; i < process.argv.length; i++) {
    array.push(parseInt(process.argv[i]));
  }
  array.sort(max);
  array.pop();
  console.log(array[array.length - 1]);
}

function max (num1, num2) {
  return num1 - num2;
}
