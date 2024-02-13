function solution(rectangle, characterX, characterY, itemX, itemY) {
    let maxX = 0, maxY = 0;
    for(let i = 0; i < rectangle.length; i++){
        maxX < rectangle[i][2] ? maxX = rectangle[i][2] : undefined;
        maxY < rectangle[i][3] ? maxY = rectangle[i][3] : undefined;
    }
    let map = new Array(maxY*2+1);
    let v = new Array(maxY*2+1);
    for(let i = 0; i < map.length; i++){
        map[i] = new Array(maxX*2+1).fill(2)
        v[i] = new Array(maxX*2+1).fill(false);
    }
    
    for(let i = 0; i < rectangle.length; i++){
        for(let j = rectangle[i][1]*2; j <= rectangle[i][3]*2; j++) {
            for(let k = rectangle[i][0]*2; k <= rectangle[i][2]*2; k++){
                if((j == rectangle[i][1]*2 || j == rectangle[i][3]*2) || (k == rectangle[i][0]*2 || k == rectangle[i][2]*2)) {
                    if(map[j][k] != 0) {
                        map[j][k] = 1
                    }
                } else {
                    map[j][k] = 0;
                }
            }
        }
    }
    let startX = characterX*2;
    let startY = characterY*2;
    let endX = itemX*2;
    let endY = itemY*2;
    v[startY][startX] = true;
    let queue = [[startY,startX,0,v]];
    while(queue.length !== 0) {
        let [y,x,value,visited] = queue.shift();
        if(y == endY && x == endX) return value/2;
        
        if(map[y][x+1] != undefined && map[y][x+1] == 1 && visited[y][x+1] == false) {
            let copy = [...visited];
            for(let i = 0; i < visited.length; i++) {
                copy[i] = [...visited[i]];
            }
            copy[y][x+1] = true;
            queue.push([y,x+1,value+1,copy])
        }
        if(map[y+1] != undefined && map[y+1][x] == 1 && visited[y+1][x] == false) {
            let copy = [...visited];
            for(let i = 0; i < visited.length; i++) {
                copy[i] = [...visited[i]];
            }
            copy[y+1][x] = true;
            queue.push([y+1,x,value+1,copy])
        }
        if(map[y][x-1] != undefined && map[y][x-1] == 1 && visited[y][x-1] == false) {
            let copy = [...visited];
            for(let i = 0; i < visited.length; i++) {
                copy[i] = [...visited[i]];
            }
            copy[y][x-1] = true;
            queue.push([y,x-1,value+1,copy])
        }
        if(map[y-1] != undefined && map[y-1][x] == 1 && visited[y-1][x] == false) {
            let copy = [...visited];
            for(let i = 0; i < visited.length; i++) {
                copy[i] = [...visited[i]];
            }
            copy[y-1][x] = true;
            queue.push([y-1,x,value+1,copy])
        }
    }

}
