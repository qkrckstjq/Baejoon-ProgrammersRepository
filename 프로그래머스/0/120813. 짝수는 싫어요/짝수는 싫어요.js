function solution(n) {
    let arr = [];
    for(let i = 1; i <= n; i++){
        i % 2 != 0 ? arr.push(i) : undefined
    }
    return arr
}