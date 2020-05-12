#!/usr/bin/node

const path = process.argv[2];
const data = process.argv[3];

const fs = require('fs');

fs.writeFile(path, data, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
