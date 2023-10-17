function solution(d, budget) {
    d.sort((a,b)=>a-b);
    let result = 0;
    for(let i = 0; i < d.length; i++) {
        if(budget >= d[i]) {
            result++;
            budget-=d[i];
        }
    }
    return result;
}