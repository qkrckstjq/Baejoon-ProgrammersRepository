function solution(n) {
    return Number(String(n).split('').sort((a,b)=> b-a).reduce((acc,cur)=>acc+=cur,""));
}