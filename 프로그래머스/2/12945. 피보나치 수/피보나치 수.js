/*let arr = []
arr[0] = 0 
arr[1] = 1
arr[2] = 1
function solution(n) {
    for(let i = 3; i <= n; i++){
        arr[i] == undefined ? arr[i] = (arr[i-1] + arr[i-2])%1234567 : undefined
    }

    return arr[n]


}*/

function solution(n) {
    const arr = [0, 1]    

  for(let i = 2; i <= n; i++){
      // j항 = j-1항 + j-2항
      // j-1항이라는 것은 결국 j항 이전을 전부 더해온 셈
      // j-2항이라는 것은 결국 j-1항 이전을 전부 더해온 셈
      // reduce? push?
      const nextValue = arr.reduce((acc, cur) => acc + cur, 0)%1234567
      arr.push(nextValue)
      // 다 더해주니까 앞의 항은 계속 컷
      arr.shift()
  }
    return arr[1]
}