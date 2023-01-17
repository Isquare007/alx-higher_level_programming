#!/usr/bin/node

const req = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
const person = {}
req(url, function(err, resp, body) {
	if (err) {
		console.log(err);
	}
	const characters = JSON.parse(body).characters;
	characters.forEach((movie) => {
		req(movie, function(err, res, body) {
			if (err) {
				console.log(err);
			}
			console.log(JSON.parse(body).name);
	});
});
});
