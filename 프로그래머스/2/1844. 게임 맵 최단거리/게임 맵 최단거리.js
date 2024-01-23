function solution(maps) {
    let v = []
    for(let i = 0; i < maps.length; i++){
        v[i] = new Array(maps[0].length).fill(false);
    }
    let queue = [[0,0,1]];
    while(queue.length !== 0) {
        let [y,x,value] = queue.shift();
        v[y][x] = true;
        if(y === maps.length-1 && x === maps[0].length-1) return value;
        if(maps[y][x+1] !== undefined && maps[y][x+1] === 1 && v[y][x+1] === false){
            queue.push([y,x+1,value+1]);
            v[y][x+1] = true;
        }
        if(maps[y+1] !== undefined && maps[y+1][x] === 1 && v[y+1][x] === false){
            queue.push([y+1,x,value+1]);
            v[y+1][x] = true;
        }
        if(maps[y][x-1] !== undefined && maps[y][x-1] === 1 && v[y][x-1] === false){
            queue.push([y,x-1,value+1]);
            v[y][x-1] = true;
        }
        if(maps[y-1] !== undefined && maps[y-1][x] === 1 && v[y-1][x] === false){
            queue.push([y-1,x,value+1]);
            v[y-1][x] = true;
        }
    }
    return -1
}

