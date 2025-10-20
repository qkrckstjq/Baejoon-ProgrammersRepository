import java.util.*;
class Solution {
    public String solution(String my_string) {
        Set<Integer> dup = new HashSet<>();
        StringBuilder answer = new StringBuilder("");
        for(int i = 0; i < my_string.length(); i++) {
            Integer c = my_string.charAt(i) - '0';
            if(dup.contains(c)) continue;
            answer.append(my_string.charAt(i));
            dup.add(c);
        }
        return answer.toString();
    }
}