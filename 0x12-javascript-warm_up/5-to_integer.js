#!/usr/bin/node
const { argv } = require('process');

if (isNaN(argv[2])) {
  console.log('Not number');
} else {
  console.log(`My number: ${parseInt(argv[2])}`);
}
