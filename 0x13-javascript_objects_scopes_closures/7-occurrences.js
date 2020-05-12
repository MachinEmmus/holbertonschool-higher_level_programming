#!/usr/bin/node
// ocurrences

exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  list.map(n => {
    if (n === searchElement) {
      occurences++;
    }
  });
  return occurences;
};
