function solution(n) {
    let sqrt = Math.floor(Math.sqrt(n));
    if(sqrt**2 === n) {
        return (sqrt+1)**2;
    } else {
        return -1
    }
    
}