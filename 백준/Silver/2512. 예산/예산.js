const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

let arr = input[1].split(' ').map(Number)
let start = 1;
let end = Math.max(...arr);
let result = 0;
const MaxCost = +input[2]

while(start <= end) {
    let mid = Math.floor((start+end)/2);
    let total = 0;
    for(let i = 0; i < arr.length; i++){
        total += mid > arr[i] ? arr[i] : mid
    }
    if(total <= MaxCost) {
        result = mid;
        start = mid + 1;
    } else {
        end = mid - 1;
    }
}
console.log(result)