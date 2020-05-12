#!/usr/bin/node
// esrever

exports.esrever = function (list) {
  const lits = [];
  for (let i = list.length - 1; i >= 0; i--) {
    lits.push(list[i]);
  }
  return lits;
};
