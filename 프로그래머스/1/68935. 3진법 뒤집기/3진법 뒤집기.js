function solution(n) {
    let reverse_three = n.toString(3).split("").reverse().join("");
    let result = 0;
    for(let i = reverse_three.length-1; i >= 0; i--) {
        result+= (reverse_three[i] * (3**(reverse_three.length - i - 1)))
    }
    return result
}
