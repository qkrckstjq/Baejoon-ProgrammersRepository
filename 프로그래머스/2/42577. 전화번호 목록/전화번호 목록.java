import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        Set<String> set = new HashSet<>();
        for(String p : phone_book) set.add(p);
        
        for(String p : phone_book) {
            String phone = "";
            for(int i = 0; i < p.length(); i++) {
                phone += Character.toString(p.charAt(i));
                if(!phone.equals(p) && set.contains(phone)) return false;
            }            
        }
        return true;
    }
}