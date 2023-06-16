#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;
  const newList = [];
  let i;
  let j;
  for (i = 0, j = len - 1; i < len && j >= 0; i++, j--) {
    newList[j] = list[i];
  }
  return newList;
};
