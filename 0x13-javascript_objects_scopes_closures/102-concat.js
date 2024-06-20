#!/usr/bin/node
const fs = require('fs');
const file1Content = fs.readFileSync(process.argv[2]);
const file2Content = fs.readFileSync(process.argv[3]);
const concatenatedContent = file1Content + file2Content;

fs.writeFileSync(process.argv[4], concatenatedContent);
