#!/usr/bin/node

const args = process.argv;
let i;
const x =  Math.floor(parseInt(args[2]));
if (!args[2]) {
  console.log('Missing number of occurrences');
} else if (isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else {
  for (i = 1; i <= x; i++) {
    console.log('C is fun');
  }
}
