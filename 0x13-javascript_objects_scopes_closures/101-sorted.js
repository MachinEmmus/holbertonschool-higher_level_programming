#!/usr/bin/node

/* ... */

const dict = require('./101-data').dict;
const listValues = Object.values(dict);
const listKeys = Object.keys(dict);
const dicty = {};
listValues.map(value => {
  dicty[value] = listKeys.filter(key => dict[key] === value);
});
console.log(dicty);
