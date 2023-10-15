function solution(arr, divisor) {
    let result = arr.sort((a,b)=>a-b).filter(item=>item%divisor===0);
    return result.length === 0 ? [-1] : result
}