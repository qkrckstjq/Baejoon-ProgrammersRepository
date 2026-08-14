function solution(arr1, arr2) {
    return arr1.map((a,idx) => {
        let b = [];
        
        for(let i = 0; i < a.length; i++){
            b.push(a[i]+arr2[idx][i]);
        }
        return b;
    })
}