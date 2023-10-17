function solution(number) {
    number.sort((a,b)=>a-b);
    let result = 0;
    for(let i = 0; i < number.length; i++) {
        for(let j = i+1; j < number.length; j++) {
            last:for(let k = j+1; k < number.length; k++) {
                // console.log(number[i], number[j], number[k], sum)
                if(number[i]+number[j]+number[number.length-1] < 0) {
                    break last;   
                }
                if(number[i]+number[j]+number[k] === 0) {
                   result++;
                }
            }
        }
    }
    return result
}