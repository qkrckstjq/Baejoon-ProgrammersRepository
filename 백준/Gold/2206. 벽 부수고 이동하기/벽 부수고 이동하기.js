// const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

// let [N, M] = input[0].split(' ');
// N = +N - 1;
// M = +M - 1;

// const [map, visited] = input.reduce((acc, cur, idx) => {
//   if(idx > 0) {
//     let data = []
//     for(let i = 0; i < cur.length; i++) {
//       if(cur[i] !== '\r') {
//         data.push(+cur[i]);
//       }
//     }
//     acc[0].push(data);
//     acc[1].push(new Array(M+1).fill(false));
//   }
//   return acc;
// }, [[], []]);

// const RY = [-1, 1, 0, 0];
// const RX = [0, 0, -1, 1];
// let result = 0;

// //y,x,뿌신여부,진행상황카운트
// const queue = [[0, 0, false,1]];
// let index = 0;
// while(queue.length - index !== 0) {
//   let [Y,X,isBk,cnt] = queue[index];
//   index++;
//   result = cnt
//   visited[Y][X] = true;
//   if(Y === N && X === M) {
//     console.log(result);
//     break;
//   }
//   for(let i = 0; i < 4; i++) {
//     let nextY = Y+RY[i];
//     let nextX = X+RX[i];
//     if(nextY >= 0 && nextY <= N && nextX >= 0 && nextX <= M) {
//       console.log(`Y:${Y} X:${X} nextY:${nextY} nextX:${nextX} isB:${isBk}\n`)
//       if(map[nextY][nextX] === 0 && !visited[nextY][nextX]){
//         queue.push([nextY,nextX,isBk,cnt+1]);
//       } else if (map[nextY][nextX] === 1 && !isBk && !visited[nextY][nextX]) {
//         queue.push([nextY,nextX,true,cnt+1]);
//       }
//     }
//   }
//   if(queue.length-index === 0) {
//     console.log(-1)
//     break;
//   }
// }

const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

let [N, M] = input[0].split(" ").map(Number);
const [map, ch] = input.reduce((acc, cur, idx) => {
    if(idx > 0) {
      let data = []
      for(let i = 0; i < cur.length; i++) {
        if(cur[i] !== '\r') {
          data.push(+cur[i]);
        }
      }
      acc[0].push(data);
      acc[1].push(new Array(M+1).fill(false));
    }
    return acc;
  }, [[], []]);
const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];
const queue = [];

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    ch[i][j] = new Array(2).fill(0);
  }
}

queue.push(0, 0, 0);
ch[0][0][0] = 1;

function BFS() {
  let idx = 0;

  while (idx !== queue.length) {
    const y= queue[idx];
    idx++;
    const x = queue[idx];
    idx++;
    const isBreak = queue[idx];

    if (x === M - 1 && y === N - 1) {
      return ch[y][x][isBreak];
    }

    for (let i = 0; i < dx.length; i++) {
      const [nx, ny] = [x + dx[i], y + dy[i]];

      if (nx >= 0 && nx < M && ny >= 0 && ny < N) {
        if (map[ny][nx] === 0 && ch[ny][nx][isBreak] === 0) {
          ch[ny][nx][isBreak] = ch[y][x][isBreak] + 1;
          queue.push(ny);
          queue.push(nx)
          queue.push(isBreak)
        } else if (map[ny][nx] === 1 && isBreak === 0) {
          ch[ny][nx][isBreak + 1] = ch[y][x][isBreak] + 1;
          queue.push(ny);
          queue.push(nx)
          queue.push(isBreak+1)
        }
      }
    }
    idx++;
  }

  return -1;
}

console.log(BFS());