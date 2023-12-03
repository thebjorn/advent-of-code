// https://adventofcode.com/2018/day/1
// part 2

import { readFileSync } from 'fs';

const digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
let values = {};
digits.forEach((digit, i) => values[digit] = i + 1);

function* range(start, end) {
    for (let i = start; i <= end; i++) yield i;
}
[...range(0, 9)].forEach(i => values["" + i] = i);

const input = readFileSync('./input.txt', 'utf8');
const inputArray = input.split('\n');

let code = 0;

const find_digits = line => {
    // zero-width positive lookahead
    const re = new RegExp(`(?=(\\d|${digits.join('|')}))`, 'g');
    const matches = Array.from(line.matchAll(re), x => x[1]);
    const vals = matches.map(n => values[n]);
    return vals[0] * 10 + vals.at(-1);
};

inputArray
    .filter(line => line.trim().length > 0)
    .forEach(line => code += find_digits(line));

console.log(code);
