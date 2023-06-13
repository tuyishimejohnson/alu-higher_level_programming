#!/usr/bin/node
const request = require('request');

// Function to fetch characters from the Star Wars API
function fetchCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  
  request(url, (error, response, body) => {
    if (response.statusCode === 200) {
      const filmData = JSON.parse(body);
      const characters = filmData.characters;
      
      // Fetch each character details
      characters.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          } else {
            console.log('Failed to fetch character data');
          }
        });
      });
    } else {
      console.log('Failed to fetch film data');
    }
  });
}

// Retrieve the movie ID from command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a movie ID as an argument');
} else {
  fetchCharacters(movieId);
}
