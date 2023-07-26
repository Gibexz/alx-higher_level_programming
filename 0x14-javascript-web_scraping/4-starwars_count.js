#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const bodyy = JSON.parse(body);
  const results = bodyy.results;
  let n = 0;

  const len = results.length;

  for (let i = 0; i < len; i++) {
    const characters = results[i].characters;

    let chars;
    for (chars of characters) {
      if (chars.endsWith('18/')) {
        n++;
      }
    }
  }
  console.log(n);
});
