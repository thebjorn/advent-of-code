// https://adventofcode.com/2018/day/1

import { readFileSync } from 'fs';

const input = readFileSync('./input.txt', 'utf8');
const inputArray = input.split('\n');

let code = 0;

const first_digit = line => line.match(/\d/)[0][0];

inputArray.filter(line => line.trim().length > 0).forEach(
    line => code += parseInt(first_digit(line) + first_digit(Array.from(line).reverse().join('')))
);

console.log(code);
