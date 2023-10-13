function solution(s){
    let p_num = 0;
    let y_num = 0;
    for(let i = 0; i <s.length; i++) {
        if(s[i].toLowerCase() === 'p') {
            p_num++;
        } else if (s[i].toLowerCase() === 'y') {
            y_num++;
        }
    }
    return p_num === y_num ? true : false;
}