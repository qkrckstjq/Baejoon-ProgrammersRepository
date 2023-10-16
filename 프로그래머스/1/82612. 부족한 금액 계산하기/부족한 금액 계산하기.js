function solution(price, money, count) {
    let sum = 0;
    for(let i = 0; i < count; i++) {
        sum += price*(i+1);
    }
    return sum > money ? sum-money : 0;
}