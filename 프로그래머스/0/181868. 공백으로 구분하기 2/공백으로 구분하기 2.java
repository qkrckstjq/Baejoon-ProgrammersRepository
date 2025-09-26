import java.util.*;
class Solution {
    public String[] solution(String my_string) {
        List<String> answer = new ArrayList<>();
        StringBuilder temp = new StringBuilder();
        for (int i = 0; i < my_string.length(); i++) {
            char c = my_string.charAt(i);
            if (c == ' ') {
                if (temp.length() > 0) {     
                    answer.add(temp.toString());
                    temp.setLength(0);       
                }
            } else {
                temp.append(c);
            }
        }
        if (temp.length() > 0) {             
            answer.add(temp.toString());
        }
        return answer.toArray(new String[0]);
    }
}