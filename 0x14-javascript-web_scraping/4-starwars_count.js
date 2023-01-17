#!/usr/bin/node

const req = require('request');
const url = process.argv[2];

req(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  let count = 0;
  const results = JSON.parse(body).results;

  for (const result of results) {
    for (const character of result.characters) {
      if (character.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
