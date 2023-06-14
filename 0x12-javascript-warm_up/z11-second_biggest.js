#!/usr/bin/node
/*
const arr = process.argv;
const len = arr.length;
let newArr = [];
for (let i = 2; i < len; i++){
	newArr[i-2] = parseInt(arr[i]);
}
//let sortedArr = newArr.sort();
//console.log(sortedArr);
let sortt = newArr.map(function(str){
	return parseInt(str);
});
sortt.sort();
console.log(sortt);
const z = 0;
if (len <= 3) {
  console.log(z);
} else {
  console.log(sortt[len - 2]);
} */

const arr = process.argv;
const len = arr.length;
const sortedArr = arr.sort();
const z = 0;
if (len <= 3) {
  console.log(z);
} else {
  console.log(sortedArr[len - 2]);
}
