import java.util.stream.*;
import java.util.*;
class Solution {
    public String[] solution(String[] picture, int k) {
        List<String> arr = Arrays.stream(picture)
            .map(str -> {
                StringBuilder s = new StringBuilder("");
                for(int i = 0; i < str.length(); i++) {
                    for(int j = 0; j < k; j++) s.append(str.charAt(i));    
                }
                return s.toString();
            }).collect(Collectors.toList());
        List<String> answer = new ArrayList<>();
        for(int i = 0; i < arr.size(); i++) {
            for(int j = 0; j < k; j++) answer.add(arr.get(i));
        }
        return answer.toArray(String[]::new);
    }
}