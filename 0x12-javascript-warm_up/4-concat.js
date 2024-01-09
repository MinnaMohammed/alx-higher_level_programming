#!/usr/bin/node
const myVar = 'is';
if (process.argv.length < 3) { console.log('undefined ${myVar} undefined'); } else if (process.argv.length === 3) { console.log('${process.argv[2]} ${myVar} undefined'); } else { console.log('${process.argv[2]} ${myVar} ${process.argv[3]}'); }
