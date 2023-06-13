#!/usr/bin/node
const request = require('request');

// Function to fetch characters of a Star Wars movie
function fetchCharacters (movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;
  
  request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;
      
      // Fetch character names
      characters.forEach(characterUrl => {
        request(characterUrl, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          } else {
            console.log('Error fetching character data:', error);
          }
        });
      });
    } else {
      console.log('Error fetching movie data:', error);
    }
  });
}

// Fetch characters of the specified movie
const movieId = process.argv[2];
fetchCharacters(movieId);
