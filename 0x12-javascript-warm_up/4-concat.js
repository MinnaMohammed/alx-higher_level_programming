#!/usr/bin/node
const var1 = process.argv[2] === undefined ? 'undefined' : process.argv[2];
const var2 = process.argv[3] === undefined ? 'undefined' : process.argv[3];
console.log(var1 + ' is ' + var2);
