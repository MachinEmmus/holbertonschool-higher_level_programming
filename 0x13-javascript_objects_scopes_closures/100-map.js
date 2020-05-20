#!/usr/bin/node
/* PUBG LITE */

const list = require('./100-data.js').list;
console.log(list);
let i = -1;
console.log(list.map(num => {
  i += 1;
  return num * i;
}));
