#!/usr/bin/node

const fs = require('fs');


try {
	const filePath = process.argv[2];
	const content = fs.readFileSync(filePath, 'utf8');
	console.log(content);
} catch (err) {
	console.log(err);
}
