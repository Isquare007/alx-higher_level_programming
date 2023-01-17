#!/usr/bin/node

const fs = require('fs');

filePath = process.argv[2]
string = process.argv[3]

fs.writeFile(filePath, string, 'utf-8', function (err) {
	if (err) {
		console.log(err);
	}
});
