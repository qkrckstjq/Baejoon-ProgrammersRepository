function solution(t, p) {
    var answer = 0;
    let i = 0;
    while(i+p.length-1 <= t.length-1) {
        let temp = "";
        for(let j = 0; j < p.length; j++) {
            temp+=t[i+j];
        }
        if(Number(temp) <= Number(p)) {
            answer++;
        }
        i++;
    }
    return answer;
}