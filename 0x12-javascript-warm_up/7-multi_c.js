#!/usr/bin/node

const args = process.argv;
let i;
const x = Math.floor(parseInt(args[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
