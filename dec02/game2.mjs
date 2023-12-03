// https://adventofcode.com/2018/day/2
// part 2

import { readFileSync } from 'fs';

const input = readFileSync('./input.txt', 'utf8');

function parse_color(rgb) {
    const tries = rgb.split(',').map(s => s.trim());
    const rgbval = tries.map(cval => cval.split(' ').reverse());
    return Object.assign(
        {red: 0, green: 0, blue: 0}, 
        Object.fromEntries(rgbval.map(v => [v[0], parseInt(v[1])]))
    );
}

function parse_colors(input) {
    return input.split(';').map(parse_color);
}

const games = input
    .split('\n').filter(line => line.trim().length > 0)
    .map(line => ({
        id: parseInt(line.match(/Game (\d+): /)[1]),
        colors: parse_colors(line.match(/: (.*)/)[1])
    }));


const maxcolors = {red: 12, green: 13, blue: 14};

const color_le = (c1, c2) => {
    for (const c in c1) {
        if (c1[c] > c2[c]) return false;
    }
    return true;
}

const mincubes = game => ({
    red: Math.max(...game.colors.map(c => c.red)),
    green: Math.max(...game.colors.map(c => c.green)),
    blue: Math.max(...game.colors.map(c => c.blue))
});

const abscubes = c => c.red * c.green * c.blue;

// 78669
console.log(
    games.map(mincubes).map(abscubes).reduce((acc, val) => acc + val, 0)
);
