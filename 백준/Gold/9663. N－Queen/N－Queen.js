const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

const N = Number(input);
let answer = 0;
let row = new Array(N).fill(0)

function check (R) {
  for(let i = 0; i < R; i++){
    if(row[R] === row[i] || R - i === Math.abs(row[R] - row[i])) {
      return false;
    }
  }
  return true;
}

function dfs (R) {
  if(R === N) {
    answer++;
  } else {
    for(let i = 0; i < N; i++) {
      row[R] = i;
      if(check(R)) {
        dfs(R+1);
      }
    }
  }
}
dfs(0)
console.log(answer)