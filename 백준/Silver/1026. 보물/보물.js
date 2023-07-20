const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

let Num = +input[0];
let A = input[1].split(' ').sort((a,b)=>Number(a)-Number(b));
let B = input[2].split(' ').sort((a,b)=>Number(b)-Number(a));
let result = 0;

for(let i = 0; i < Num; i++) {
    result += Number(A[i])*Number(B[i]);
}

console.log(result)