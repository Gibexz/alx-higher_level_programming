#!/usr/bin/node

const args = process.argv;
let i;

if (!args[2]) {
	console.log('Missing number of occurrences');
} else if (isNaN(args[2])) {
	console.log('Missing number of occurrences');
} else {
	for (i = 1; i <= Math.floor(parseInt(args[2])); i++) {
		console.log('C is fun');
	}
}
