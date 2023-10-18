function solution(n, arr1, arr2) {
    let sum_arr = [];
    for(let i = 0; i < n; i++) {
        let line = "";
        let b1 = arr1[i].toString(2);
        let b2 = arr2[i].toString(2);
        if(b1.length < n) {
            let fill = "";
            for(let j = 0; j < n - b1.length; j++) {
                fill+="0";
            }
            let temp = b1;
            b1 = fill + temp;
        }
        if(b2.length < n) {
            let fill = "";
            for(let j = 0; j < n - b2.length; j++) {
                fill+="0";
            }
            let temp = b2;
            b2 = fill + temp;
        }
        for(let j = 0; j < n; j++) {            
            if(b1[j] === "1" || b2[j] === "1") {
                line+="#";
            } else {
                line+=" ";
            }
        }
        sum_arr.push(line);
    }
    return sum_arr;
}