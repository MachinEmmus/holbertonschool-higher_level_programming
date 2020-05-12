#!/usr/bin/node

const request = require('request');
const path = process.argv[2];
const dicty = {};

request(path, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    const response = JSON.parse(body);

    for (let i = 0; i < response.length; i++) {
      if (response[i].completed === true) {
        if (dicty[response[i].userId] === undefined) {
          dicty[response[i].userId] = 1;
        } else {
          dicty[response[i].userId] += 1;
        }
      }
    }
  }
  console.log(dicty);
});
