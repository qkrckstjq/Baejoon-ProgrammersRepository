function solution(s) {
    let result = "";
    const sample = ["zero","one","two","three","four","five","six","seven","eight","nine"];
    function findN (w) {        
        for(let i = 0; i < sample.length; i++) {
            if(w === sample[i]) {
                return true;
            }
        }
        return false;
    }
    for(let i = 0; i < s.length; i++) {
        let word = "";
        if(isNaN(Number(s[i]))) {
            while(isNaN(Number(s[i])) && !findN(word)) {
                word+=s[i];
                i++;
            }
            console.log(word)
            for(let k = 0; k < sample.length; k++) {
                if(sample[k] === word) {
                    result+=String(k);
                }
            }
            i--;
        } else {
            result+=s[i];
        }
    }
    return Number(result);
}