function solution(a, b) {
    let min = a <= b ? a : b;
    let max = a <= b ? b : a;
    return (min+max)*(max-min+1)/2;
}