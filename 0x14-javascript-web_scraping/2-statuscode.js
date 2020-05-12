#!/usr/bin/node

const path = process.argv[2];
const request = require('request');

request(path, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
