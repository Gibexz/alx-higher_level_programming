#!/usr/bin/node

const args = process.argv;
let i;
const x = Math.floor(parseInt(args[2]));
const str = 'X';
const strCount = str.repeat(x);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (i = 0; i < x; i++) {
    console.log(strCount);
  }
}
