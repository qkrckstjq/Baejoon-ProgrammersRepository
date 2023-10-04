const fs = require('fs');
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./test.txt").toString().trim().split(" ");

const AB = Number(input[0]+input[1]);
const CD = Number(input[2]+input[3]);
console.log(AB+CD);