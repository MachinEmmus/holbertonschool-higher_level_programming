#!/usr/bin/node
// LogMe
const logMe = require('./9-logme').logMe;

let numArgPrinted = 0;
exports.logMe = function (item) {
  console.log(numArgPrinted + ': ' + item);
  numArgPrinted++;
};
