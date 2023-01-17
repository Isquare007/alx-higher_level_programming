#!/usr/bin/node

const req = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

req(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  }
  const i = 0;
  const characters = JSON.parse(body).characters;

  printName(characters, i);
});
const printName = function (url, i) {
  req(url[i], function (err, res, body) {
    if (err) {
      console.log(err);
    }
    console.log(JSON.parse(body).name);
    if (++i < url.length) {
      printName(url, i++);
    }
  });
};
