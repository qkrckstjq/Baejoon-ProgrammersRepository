const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

const [row, col] = input[0].split(' ');
const queue = [];
let queue_idx = 0;

const [map,visited] = input.reduce((acc,cur,idx)=>{
    if(idx > 0) {
        const arr = [];
        const V = [];
        cur.split(' ').map((el,index)=>{
            arr.push(Number(el))
            if(el == 1 || el == 0) {
                if(el == 1){
                    queue.push([idx-1, index, 0]);
                };
                V.push(false);
            } else if (el == -1) {
                V.push(undefined);
            }
        });
        acc[1].push(V);
        acc[0].push(arr);
    }
    return acc;
},[[],[]]);

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

let date = 0;

while(queue.length-queue_idx !== 0) {
    const [y, x, d] = queue[queue_idx];
    queue_idx+=1
    date = d;
    map[y][x] = 1;
    visited[y][x] = true;

    for (let i = 0; i < 4; i++) {
        const ny = y + dy[i];
        const nx = x + dx[i];

        if (ny >= 0 && ny < col && nx >= 0 && nx < row && map[ny][nx] === 0 && !visited[ny][nx]) {
            queue.push([ny, nx, date + 1]);
            visited[ny][nx] = true;
        }
    }
}

findzero:for (let i = 0; i < col; i++) {
    for (let j = 0; j < row; j++) {
        if (map[i][j] === 0) {
            date = -1;
            break findzero;
        }
    }
}

console.log(date);