#!/usr/bin/node
/* LogMe */

let numArgPrinted = 0;
exports.logMe = function (item) {
  console.log(numArgPrinted + ': ' + item);
  numArgPrinted++;
};
