#!/usr/bin/node
// Global scope
let argsCnt = 0;
exports.logMe = function (item) {
  console.log(`${argsCnt}: ${item}`);
  argsCnt++;
};
