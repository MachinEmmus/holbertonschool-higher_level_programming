#!/usr/bin/node
/* Concats two files */

const args = process.argv.slice(2);
const fs = require('fs');

fs.readFile(args[0], 'utf-8', (err, fileA) => {
  if (err) console.log(err);
  fs.readFile(args[1], 'utf-8', (err, fileB) => {
    if (err) console.log(err);
    fs.writeFile(args[2], fileA + fileB, (err) => {
      if (err) console.log(err);
    });
  });
});
