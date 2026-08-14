function solution(arr) {
  let sum = 0;
    for(let i = 0; i < arr.length; i++){
        sum+=arr[i];
    }
    return sum/arr.length
    
}
//  보자마자 든 생각
//  배열안의 모든 값의 합을 구해야겠다.
//  배열을 다 더한 값을 arr.length 나눠주면 되겠따.


// function solution(arr) {
//   const average = arr.reduce((acc,cur,index,arr)=>{
//    return index === (arr.length -1) ? (acc+cur)/arr.length :  acc+cur
//   },0)
//   return average
// }