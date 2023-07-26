#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const todos = JSON.parse(body);
  const uniqueUserIds = new Set();
  todos.forEach(entry => {
    uniqueUserIds.add(entry.userId);
  });
  const numUniqueUserIds = uniqueUserIds.size;

  const completed = {};
  for (let i = 1; i <= numUniqueUserIds; i++) {
    let n = 0;
    for (const dos of todos) {
      if (dos.userId === i && dos.completed === true) {
        n++;
      }
    }
    completed[i] = n;
  }
  console.log(completed);
});
