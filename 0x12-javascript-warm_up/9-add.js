#!/usr/bin/node
function add (a, b) {
  const v1 = parseInt(Number(a));
  const v2 = parseInt(Number(b));
  console.log(v1 + v2);
}
add(process.argv[2], process.argv[3]);
