#!/usr/bin/node
/* PUBG LITE */

const list = require('./100-data.js').list;
console.log(list);
let index = -1;
console.log(list.map(num => {
  index += 1;
  return num * index;
}));
