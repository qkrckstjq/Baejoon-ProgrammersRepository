const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

let data = input.slice(1).map((el) => el.replace(/\r/g,"").split(''));
let ans = ''
function pseudosocialSentence(arr) {
    let count = 0;
    let left = 0;
    let right = arr.length - 1;
    while(left < right) {
        if(arr[left] !== arr[right] && count > 0) {
            return 2
        }
        if(arr[left] !== arr[right] && count < 1) {
            if(arr[left+1] === arr[right]) {
                count++;
                let isPesudo = true;
                let i=left+1,j=right;
                while(i < j) {
                    if(arr[i] !== arr[j]) {
                        isPesudo = false;
                        break
                    };
                    i++,j--;
                }
                if(isPesudo){
                    return 1
                }
            }
            if (arr[left] === arr[right-1]) {
                count++;
                let isPesudo = true;
                let i=left,j=right-1;
                while(i < j) {
                    if(arr[i] !== arr[j]) {
                        isPesudo = false;
                        break
                    };
                    i++,j--;
                }
                if(isPesudo){
                    return 1
                }
            }
            if (arr[left+1] !== arr[right] || arr[left] !== arr[right-1]){
                return 2
            }
        }
        left++,right--;
    }
    return 0;
}

for(let i = 0; i < data.length; i++){
    ans+=`${pseudosocialSentence(data[i])}\n`
}

console.log(ans)