import java.util.*;
class Solution {
    public String[] solution(String my_string) {
        String[] answer = new String[my_string.length()];
        for(int i = 0; i < my_string.length(); i++) {
            StringBuilder temp = new StringBuilder("");
            for(int j = i; j < my_string.length(); j++){
                temp.append(my_string.charAt(j));
            }
            answer[i] = temp.toString();
        }
        Arrays.sort(answer);
        return answer;
    }
}