function solution(s){
    let count = 0;
    for(let i = 0; i < s.length; i++){
        s.charAt(i) == '(' ? count++ : count--;
        if(count < 0){
            return false
        }   
    }
    return count == 0 ? true : false
}