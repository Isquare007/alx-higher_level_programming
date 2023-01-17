#!/usr/bin/node

const req = require('request');
const url = process.argv[2];

req(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }

  const todos = JSON.parse(body);
  const info = {};

  for (const tasks of todos) {
    if (tasks.completed && info[tasks.userId] === undefined) {
      info[tasks.userId] = 1;
    } else if (tasks.completed) {
      info[tasks.userId] += 1;
    }
  }
  console.log(info);
});
