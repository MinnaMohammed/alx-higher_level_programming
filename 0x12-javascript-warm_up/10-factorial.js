#!/usr/bin/node
const computeFactorial = (n) => {
  n = parseInt(n, 10);
  if (isNaN(n)) return 1;
  if (n <= 1) return 1;
  return n * computeFactorial(n - 1);
};
const num = process.argv[2];
const factorial = computeFactorial(num);
console.log(factorial);
