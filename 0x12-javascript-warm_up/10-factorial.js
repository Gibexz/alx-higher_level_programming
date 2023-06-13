#!/usr/bin/node

const arg = parseInt(process.argv[2]);
function factorial (num) {
  if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
if (isNaN(arg)) {
  console.log('1');
} else {
  console.log(factorial(arg));
}
