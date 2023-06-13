#!/usr/bin/node

const arr = process.argv;
const len = arr.length;
const sortedArr = arr.sort();
const z = 0;
if (len <= 3) {
  console.log(z);
} else {
  console.log(sortedArr[len - 2]);
}
