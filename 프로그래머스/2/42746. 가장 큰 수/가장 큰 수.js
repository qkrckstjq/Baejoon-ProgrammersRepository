function solution(numbers) {
  // 숫자 배열을 문자열 배열로 변환
  const strArr = numbers.map(num => String(num));
  
  // 문자열을 이어 붙여 비교하는 함수
  const compareFunc = (a, b) => {
    return Number(b + a) - Number(a + b);
  };
  
  // 문자열을 이어 붙인 후, 내림차순으로 정렬
  strArr.sort(compareFunc);
  
  // 0으로만 구성된 문자열인 경우 "0"을 반환, 그 외에는 숫자로 변환하여 반환
  return strArr[0] === "0" ? "0" : strArr.join("");
}