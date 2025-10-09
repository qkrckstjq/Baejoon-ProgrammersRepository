import java.util.*;
class Solution {
    public Map<String, String> map = new HashMap<>();
    public long solution(String numbers) {
        map.put("zero", "0");
        map.put("one", "1");
        map.put("two", "2");
        map.put("three", "3");
        map.put("four", "4");
        map.put("five", "5");
        map.put("six", "6");
        map.put("seven", "7");
        map.put("eight", "8");
        map.put("nine", "9");
        StringBuilder answer = new StringBuilder("");
        StringBuilder temp = new StringBuilder("");
                
        for(int i = 0; i < numbers.length(); i++) {
            temp.append(numbers.charAt(i));
            if(map.containsKey(temp.toString())) {
                answer.append(map.get(temp.toString()));
                temp = new StringBuilder("");
            }
        }
        // System.out.println(answer.toString());
        long result = 0L;
        int index = 0;
        for(int i = answer.length() - 1; i >= 0; i--) {
            result += (answer.charAt(i) - '0') * Math.pow(10, index++);
        }
        return result;
    }
}