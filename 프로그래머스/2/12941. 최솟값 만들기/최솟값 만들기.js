function solution(A,B){
    B.sort((a,b)=>b-a)
    A.sort((a,b)=>a-b)
    return A.reduce((acc,_,i)=> acc+(A[i]*B[i]),0)
}