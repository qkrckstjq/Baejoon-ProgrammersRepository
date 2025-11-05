import java.util.*;
import java.util.stream.*;
class Solution {
    public String solution(String letter) {
        Map<String, String> map = new HashMap<>();
        String[] mors = new String[]{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        for(int i = 0; i < mors.length; i++) {
            map.put(mors[i], Character.toString(97 + i));
        }
        
        StringBuilder answer = new StringBuilder("");
        StringBuilder temp = new StringBuilder("");
        for (int i = 0; i < letter.length(); i++) {
            char c = letter.charAt(i);
            if (c == ' ') {
                answer.append(map.get(temp.toString()));
                temp.setLength(0);
            } else {
                temp.append(c);
            }
        }

        // 마지막 조각 처리
        if (temp.length() > 0) {
            answer.append(map.get(temp.toString()));
        }
        
        return answer.toString();
    }
}