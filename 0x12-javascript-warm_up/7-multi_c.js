#!/usr/bin/node

const args = process.argv;
let i;

if (!args[2]) {
  console.log('Missing number of occurrences');
} else if (isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else if (!isNaN(args[2])) {
  for (i = 1; i <= parseInt(args[2]); i++) {
    console.log('C is fun');
  }
}
