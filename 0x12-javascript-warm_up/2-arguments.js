#!/usr/bin/node
const args = process.argv.length;
if (args < 3) {
  consoole.log('No argument');
} else if (args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
