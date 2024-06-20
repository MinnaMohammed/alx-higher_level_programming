#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let cnt = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    newList[i] = list[cnt];
    cnt++;
  }
  return newList;
};
