#!/usr/bin/node

fs = require('fs')

req = require('request');
url = process.argv[2];
filePath = process.argv[3];

req(url, function(err, response, body) {
	if (err) {
		console.log(err)
	}
	fs.writeFile(filePath, body, 'utf-8', function (err) {
		if (err) {
			console.log(err)
		}
	})
})
