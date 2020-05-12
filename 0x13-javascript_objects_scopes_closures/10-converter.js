#!/usr/bin/node
// save the gun

exports.converter = function (base) {
  return (num) => num.toString(base);
};
