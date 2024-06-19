#!/usr/bin/node
const str = process.argv[2];
const intVal = parseInt(Number(str));
if (isNaN(intVal)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < intVal; x++) {
    console.log('C is fun');
  }
}
