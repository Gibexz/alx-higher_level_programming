#!/usr/bin/node

const args = process.argv;
let i;
const x = Math.floor(Number(args[2]));
if (!x) {
  console.log('Missing number of occurrences');
} else if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 1; i <= x; i++) {
    console.log('C is fun');
  }
}
