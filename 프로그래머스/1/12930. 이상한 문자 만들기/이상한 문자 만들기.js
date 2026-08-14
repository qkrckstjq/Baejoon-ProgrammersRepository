function solution(s) {
    let result = ''
    let str_arr = s.split(' ');
    for(let i = 0; i < str_arr.length; i++){
        for(let j = 0; j < str_arr[i].length; j++){
            if(j % 2 == 0){
                result+=str_arr[i][j].toUpperCase();
            } else {
                result+=str_arr[i][j].toLowerCase();
            }
        }
        if(i != str_arr.length-1){
            result+=' ';    
        }
    }
    return result;
}