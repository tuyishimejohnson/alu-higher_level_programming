#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

const baseUrl = 'https://swapi.dev/api';
const filmsUrl = `${baseUrl}/films`;

request(filmsUrl, function(error, response, body) {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const selectedFilm = films.find(film => film.episode_id === parseInt(movieId));
    
    if (selectedFilm) {
      const charactersUrls = selectedFilm.characters;
      const charactersCount = charactersUrls.length;
      let charactersProcessed = 0;
      
      charactersUrls.forEach(characterUrl => {
        request(characterUrl, function(error, response, body) {
          if (!error && response.statusCode === 200) {
            const character = JSON.parse(body).name;
            console.log(character);
          }
          
          charactersProcessed++;
          
          if (charactersProcessed === charactersCount) {
            process.exit(0);
          }
        });
      });
    } else {
      console.log('Movie not found.');
      process.exit(1);
    }
  } else {
    console.log('Error retrieving film data.');
    process.exit(1);
  }
});
