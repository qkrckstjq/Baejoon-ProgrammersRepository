function solution(arr) {
    let min = arr[0];
    let idx = 0;
    for(let i = 1; i < arr.length; i++) {
        if(min > arr[i]) {
            min = arr[i];
            idx = i;
        }
    }
    arr.splice(idx,1);
    return arr.length === 0 ? [-1] : arr;
}
