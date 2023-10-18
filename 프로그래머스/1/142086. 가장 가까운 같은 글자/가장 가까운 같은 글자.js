function solution(s) {
    let result = [];
    let history = {};
    for(let i = 0; i < s.length; i++) {
        if(history[s[i]] !== undefined) {
            result.push(i - history[s[i]]);
            history[s[i]] = i;
        } else {
            result.push(-1);
            history[s[i]] = i;
        }
    }
    return result;
}