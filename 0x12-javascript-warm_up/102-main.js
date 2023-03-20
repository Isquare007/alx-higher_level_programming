#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(5, function (nub) {
  console.log('New value: ' + nub);
});
