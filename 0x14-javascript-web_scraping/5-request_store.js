#!/usr/bin/node

const fs = require('fs');

const req = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

req(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(filePath, body, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
