function solution(s, n) {
    var answer = '';
    for(let i = 0; i < s.length; i++) {
        if(65 <= s[i].charCodeAt(0) && s[i].charCodeAt(0) <= 90) {
            if(s[i].charCodeAt(0)+n > 90) {
                answer+=String.fromCharCode(65 + n - (91 -  s[i].charCodeAt(0)));
            } else {
                answer+=String.fromCharCode(s[i].charCodeAt(0)+n);
            }
        } else if (97 <= s[i].charCodeAt(0) && s[i].charCodeAt(0) <= 122) {
            if(s[i].charCodeAt(0)+n > 122) {
                answer+=String.fromCharCode(97 + n - (123 -  s[i].charCodeAt(0)));
            } else {
                answer+=String.fromCharCode(s[i].charCodeAt(0)+n);
            }
        } else {
            answer+=" ";
        }
    }
    return answer;
}