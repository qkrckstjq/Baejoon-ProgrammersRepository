import java.util.*;
class Solution {
    public String[] solution(String[] str_list) {
        List<String> temp = new ArrayList<>();
        boolean first = true;
        boolean hit = false;
        for(int i = 0; i < str_list.length; i++) {
            if(first && str_list[i].equals("l")) {
                first = false;
                hit = true;
                break;
            } else if(first && str_list[i].equals("r")) {
                temp = new ArrayList<>();
                first = false;
                hit = true;
                continue;
            }
            temp.add(str_list[i]);
        }
        if(!hit) {
            return new String[0];
        }
        return temp.toArray(new String[0]);
    }
}