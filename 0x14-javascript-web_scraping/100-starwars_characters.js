#!/usr/bin/node

const request = require('request');
const args = process.argv[2];
const uri = `https://swapi-api.hbtn.io/api/films/${args}`;

request(uri, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const charactersUri = JSON.parse(body).characters;

    charactersUri.forEach(characterUri => {
      request(characterUri, (err, resp, body) => {
        if (err) {
          console.error(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
