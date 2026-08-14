function solution(array) {
  const obj = {};
  let maxNum = 0, ans = 0, boolean = 0;
  array.forEach((el) => {
    !obj[el] ? obj[el] = 1 : obj[el]++;
    maxNum < obj[el] ? (maxNum = obj[el], ans = el, boolean = 0) : maxNum == obj[el] ? boolean = 1 : undefined;
  });
    return boolean == 1 ? -1 : ans
}