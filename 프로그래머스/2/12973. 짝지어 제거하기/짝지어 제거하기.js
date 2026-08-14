function solution(s){
   const stack = [];
  
  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    
    if (stack.length > 0 && stack[stack.length - 1] === char) {
      stack.pop(); // 짝이 맞으면 스택에서 제거
    } else {
      stack.push(char); // 짝이 아니면 스택에 추가
    }
  }
  
  return stack.length === 0 ? 1 : 0; // 스택이 비어있으면 1, 아니면 0 반환
    
}