#!/usr/bin/node
const fs = require('fs');
let myVar = 333;
const data = `var myVar = ${myVar};`;
const filePath = 'path/to/your/file.js';
fs.writeFile(filePath, data, 'utf8', (err) => {
  if (err) {
    console.error('Error writing to file:', err);
  } else {
    console.log('Value of myVar has been modified and saved to the file.');
  }
});
