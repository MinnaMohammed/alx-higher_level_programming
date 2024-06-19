#!/usr/bin/node
const str = process.argv[2];
const intVal = Number(str);
if (isNaN(intVal)) {
  console.log('Not a number');
} else {
  console.log(parseInt(intVal));
}
