#!/usr/bin/node

const request = require('request');
const cap = process.argv[2];
const path = 'http://swapi.co/api/films/' + cap + '/';

request.get(path, function (err, response, body) {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
