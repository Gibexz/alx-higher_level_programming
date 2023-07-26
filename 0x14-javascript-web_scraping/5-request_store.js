#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const content = body;

  const file = process.argv[3];
  const fs = require('fs');
  fs.writeFile(file, content, 'utf-8', err => {
    if (err) {
      console.error(err);
    }
  });
});
