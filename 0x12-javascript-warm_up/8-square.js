#!/usr/bin/node
const num = process.argv[2];
let x = '';

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    x = '';
    for (let j = 0; j < num; j++) {
      x = x + 'X';
    }
    console.log(x);
  }
}
