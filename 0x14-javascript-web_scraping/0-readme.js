#!/usr/bin/node

const fs = require('fs');

const files = process.argv[2];

fs.readFile(files, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
