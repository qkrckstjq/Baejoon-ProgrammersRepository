const { ALL } = require("dns");
const fs = require("fs");
const { start } = require("repl");
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split("\n");

const info = input[0].split(' ').map(el=>Number(el))
const Alledges = input.slice(1).map(el=>el.split(' ').map(el2=>Number(el2)));

const MaxNode = info[0]+1;
const startNode = info[2];
const map = new Array(MaxNode);
const DFS_V = new Array(MaxNode).fill(false);
const BFS_V = new Array(MaxNode).fill(false);
const stack = [];
const queue = [];
let dfs = '';
let bfs = '';

for(let i = 0; i < MaxNode; i++) {
    map[i] = new Array(MaxNode).fill(0);
}

for(let i = 0; i < Alledges.length; i++){
    map[Alledges[i][0]][Alledges[i][1]] = 1;
    map[Alledges[i][1]][Alledges[i][0]] = 1;
}

stack.push(startNode);
queue.push(startNode);

while(stack.length !== 0 || queue.length !== 0) {
    if(stack.length !== 0) {
        let DFSNode = stack.pop();
        if(!DFS_V[DFSNode]) {
            dfs+=DFSNode+' ';
        }
        DFS_V[DFSNode] = true;
        for(let i = map[DFSNode].length; i >= 0; i--) {
            if(map[DFSNode][i] === 1 && !DFS_V[i]) {
                stack.push(i);
            }
        }
    }
    if(queue.length !== 0) {
        let BFSNode = queue.shift();
        if(!BFS_V[BFSNode]) {
            bfs+=BFSNode+' ';
        }
        BFS_V[BFSNode] = true;
        for(let i = 1; i < map[BFSNode].length; i++) {
            if(map[BFSNode][i] === 1 && !BFS_V[i]) {
                queue.push(i);
            }
        }
    }
}
let result = `${dfs}\n${bfs}`
console.log(result)