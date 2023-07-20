const { sign } = require('crypto');

const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

const [n, m] = input[0].split(' ');
let [N, M] = [Number(n), Number(m)];
const [Bundle, Single] = input.reduce((acc,cur,idx)=>{
    const [a,b] = cur.split(' ');
    if(idx > 0) {
        if(acc[0] > Number(a)) {
            acc[0] = Number(a);
        }
        if(acc[1] > Number(b)) {
            acc[1] = Number(b);
        }
    }
    return acc;
},[1000, 1000])

let result = 0;
while(N > 0) {
    if(N >= 6) {
        if(Bundle > Single*6) {
            result += Single*6;
        } else {
            result += Bundle;
        }
    } else {
        if(Bundle > Single*N) {
            let rest = N;
            result += Single*rest;
        } else {
            result += Bundle;
        }
    }
    N-=6;
}
console.log(result)