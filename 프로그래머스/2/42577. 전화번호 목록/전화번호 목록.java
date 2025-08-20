import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Set<String> phoneNumbers = new HashSet<>();
        for(String num : phone_book) {
            phoneNumbers.add(num);
        }
        
        for(String number : phone_book) {
            String temp = "";
            for(int i = 0; i < number.length() - 1; i++) {
                temp += number.charAt(i);
                if (phoneNumbers.contains(temp)) {
                    System.out.println(temp);
                    return false;
                }
            }
        }
        
        return true;
    }
}