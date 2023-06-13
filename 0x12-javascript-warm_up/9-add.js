#!/usr/bin/node

const args = process.argv;
const first = parseInt(args[2]);
const sec = parseInt(args[3]);

function add (a, b) {
  const c = a + b;
  console.log(c);
}
add(first, sec);
