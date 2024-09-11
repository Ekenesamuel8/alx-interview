#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
    console.log("Usage: node 0-starwars_characters.js <Movie ID>");
    process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, { json: true }, (err, res, body) => {
    if (err) {
        return console.error('Error:', err);
    }
    if (res.statusCode !== 200) {
        return console.error('Failed to retrieve movie:', res.statusCode);
    }

    const characters = body.characters;

    function fetchCharacter(index) {
        if (index >= characters.length) return; // Exit condition

        request(characters[index], { json: true }, (err, res, body) => {
            if (err) {
                return console.error('Error:', err);
            }
            console.log(body.name);
            fetchCharacter(index + 1); // Fetch the next character
        });
    }

    fetchCharacter(0); // Start fetching characters from the first one
});

