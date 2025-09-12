import java.util.*;
class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        List<Integer> answer = new ArrayList<>();
        for(int i = 0; i < intStrs.length; i++) {
            StringBuilder temp = new StringBuilder("");
            for(int j = s; j < s + l; j++) {
                temp.append(intStrs[i].charAt(j));
            }
            Integer tempValue = Integer.parseInt(temp.toString());
            if(tempValue > k) {
                answer.add(tempValue);
            }
        }
        int[] result = new int[answer.size()];
        for(int i = 0; i < answer.size(); i++) {
            result[i] = answer.get(i);
        }
    
        return result;
    }
}