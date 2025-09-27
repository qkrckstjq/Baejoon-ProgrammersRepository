import java.util.*;
class Solution {
    public String[] solution(String myStr) {
        List<String> answer = new ArrayList<>();
        StringBuilder temp = new StringBuilder("");
        for(int i = 0; i < myStr.length(); i++) {
            char c = myStr.charAt(i);
            if(c == 'a' || c == 'b' || c == 'c') {
                if(temp.length() != 0) {
                    answer.add(temp.toString());
                    temp = new StringBuilder("");
                }
                continue;    
            }
            temp.append(c);    
        }
        if(temp.length() != 0) answer.add(temp.toString());
        if(answer.isEmpty()) answer.add("EMPTY");
        return answer.stream().toArray(String[]::new);
    }
}