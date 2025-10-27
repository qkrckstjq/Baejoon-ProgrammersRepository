import java.util.*;
class Solution {
    public int[] solution(int n) {
        List<Integer> answer = new ArrayList<>();
        int num = 2;
        while(num <= n) {
            if(n % num == 0) answer.add(num);
            while(n % num == 0) {
                n /= num;
            }
            num += 1;
        }
        return answer.stream().mapToInt(q -> q).toArray();
    }
}