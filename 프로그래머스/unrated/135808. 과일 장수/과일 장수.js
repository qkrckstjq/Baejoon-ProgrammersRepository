// const qk = (arr) => {
//     let fiv = arr[0];
//     let left = [];
//     let right = [];
//     for(let i = 1; i < arr.lenght; i++) {
//         arr[i] > fiv ? 
//     }
// }

function solution(k, m, score) {
    let sortedArr = score.sort((a,b)=>b-a);
    let result = 0;
    for(let i = (m-1); i < sortedArr.length; i+=m) {
        if(sortedArr[i] !== undefined) {
            result+=(sortedArr[i]*m);
        }
    }
    return result
}