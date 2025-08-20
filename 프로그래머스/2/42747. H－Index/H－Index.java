import java.util.*;
class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        int[] reverse = new int[citations.length];
        for(int i = citations.length - 1; i >= 0; i--) {
            reverse[citations.length - 1 - i] = citations[i];
        }
        
        int answer = 0;
        for(int i = 0; i < citations.length; i++) {
            if(i + 1 <= reverse[i]) {
                answer = (i + 1);
            } else {
                break;
            }
        }
        return answer;
    }
}