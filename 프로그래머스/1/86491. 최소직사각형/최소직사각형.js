function solution(sizes) {
    let vert = 0;
    let hori = 0;
    for(let i = 0; i < sizes.length; i++) {
        if(sizes[i][0] < sizes[i][1]) {
            let temp = sizes[i][0];
            sizes[i][0] = sizes[i][1];
            sizes[i][1] = temp;
        }
        vert = vert < sizes[i][0] ? sizes[i][0] : vert;
        hori = hori < sizes[i][1] ? sizes[i][1] : hori;
    }
    return vert*hori
}