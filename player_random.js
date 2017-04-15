#!/usr/bin/env node

var readline = require('readline');
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

rl.on('line', function(line){
    parts = line.split(' ');
    if (parts[0] == 'NEW_ROUND') {
        quantity = 0;
        value = 6;
    } else if (parts[0] == 'PLAYER_BIDS') {
        quantity = parseInt(parts[2]);
        value = parseInt(parts[3]);
    } else if (parts[0] == 'PLAY') {
        if (quantity > 0 && Math.random() < 0.4) {
            console.log('CHALLENGE');
        } else {
            console.log('BID ' + (quantity+1) + ' ' + value);
        }
    }
})
