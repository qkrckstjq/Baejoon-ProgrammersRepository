function gcd (a,b) {
    while(b !== 0) {
        [a,b] = [b, a%b];
    }
    return a;
}

function solution(n, m) {
    let min = gcd(n,m)
    return [min, n*m/min ]
}