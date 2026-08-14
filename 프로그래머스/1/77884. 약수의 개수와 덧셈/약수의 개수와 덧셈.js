function solution(left, right) {
    let sum = 0;                                 //sum==result
    let count = 0;                               //약수의 개수
    //left = 13, right = 17
    for(let i = left; i <= right; i++){         // left부터 right작거나같아질때까지 1씩 커진다
        count = 0;
        //i = 17, 17 % 1 == 0 count = 2 
        for(let j = 1; j <= i; j++){            // 1부터 i까지 작거나같아질때까지 1씩 커진다
            i % j == 0 ? count++ : undefined    //i%j가 0이면 j는 i의 약수다 그러면 count++
        }
                                                  // for문이 끝나고 나면 count는 무엇을 의미할까요????
        count % 2 == 0 ? sum+=i : sum-=i;       // count는 i의 약수의 개수
    }               
    return sum;
}