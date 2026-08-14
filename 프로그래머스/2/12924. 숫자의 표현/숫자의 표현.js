function solution(n) {
  let count = 0;
  let start = 1;

  while (start <= n) {
    let sum = 0;
    for (let i = start; sum < n; i++) {
      sum += i;
      if (sum === n) {
        count++;
        break;
      } else if (sum > n) {
        break;
      }
    }
    start++;
  }

  return count;
}