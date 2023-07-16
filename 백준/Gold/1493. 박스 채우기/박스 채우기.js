const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const [len,wid,hei] = input[0].split(' ').map(el=>Number(el))
const cube = input.slice(2).map(el=> el.split(' ').map((item,idx)=>idx===0 ? Number(2**item) : Number(item) ) );
let answer = 0;
let NoMore;
let stack = [];

stack.push(len,wid,hei);

while(stack.length !== 0) {
    let l=stack.pop(),w=stack.pop(),h=stack.pop();
    NoMore = true;
    let Max = Math.min(l,w,h);
    for(let i = cube.length-1; i >= 0; i--) {
        if(cube[i][0] <= Max && cube[i][1] !== 0) {
            answer++;
            cube[i][1]--;
            Max = cube[i][0];
            NoMore = false;
            break;
        }
    }
    if(NoMore) break;
    if(w-Max !== 0) {stack.push(Max,w-Max,Max)}
    if(l-Max !== 0) {stack.push(l-Max,w,Max)}
    if(h-Max !== 0) {stack.push(l,w,h-Max)}
}

console.log(NoMore ? -1 : answer)