function solution (n,edge){
    let start = 1;
    let d = [0];
    let obj = {}
    for(let i = 0; i < edge.length; i++){
        if(obj[edge[i][0]]) {
            obj[edge[i][0]].push(edge[i][1])
        } else {
            obj[edge[i][0]] = [edge[i][1]]
        }
        if(obj[edge[i][1]]) {
            obj[edge[i][1]].push(edge[i][0])
        } else {
            obj[edge[i][1]] = [edge[i][0]]
        }
    }
    let Novisited = -1;
    let next_node = [1];
    for(let i = 1; i <= n; i++) {
        d[i] = Novisited;
    }
    d[start] = 0;
    while(next_node.length != 0) {
        let node = next_node.shift();
        let v = obj[node];
        for(let i = 0; i < v.length; i++){
            if(d[v[i]] == Novisited) {
                d[v[i]] = d[node] + 1;
                next_node.push(v[i])
            }
        }
    }
    let max_num = Math.max(...d);
    let answer = 0;
    for(let i = 0; i < d.length; i++){
        if(max_num == d[i]) {
            answer++;
        }
    }
    return answer
}
