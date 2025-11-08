import java.util.stream.*;
class Solution {
    public int solution(int n) {
        boolean[] primeArr = new boolean[101];
        for(int i = 2; i < (int) Math.sqrt(101); i++) {
            if(!primeArr[i]) {
                for(int j = i * i; j < 101; j += i) {
                    primeArr[j] = true;
                } 
            }
        }
        return IntStream.range(0, n + 1)
            .boxed()
            .reduce(0, (result, i) -> (result + (primeArr[i] ? 1 : 0)));
    }
}