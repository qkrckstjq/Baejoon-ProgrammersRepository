function solution(arr) {
    let result = [];
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] !== result[result.length ? result.length-1 : 0]) {
            result.push(arr[i]);
        }
    }
    return result
}