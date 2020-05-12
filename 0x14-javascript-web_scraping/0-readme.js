#!/usr/bin/node
const path = process.argv[2];

const fs = require('fs');

fs.readFile(path, { encoding: 'utf8' }, (error, data) => {
  if (error) { console.log(error); } else { console.log(data); }
});
