import java.util.HashMap;
import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        int[] answer = {1,3};
        String[] splitedToday = today.split("\\.");
        int[] IntegerToday = new int[3];
        HashMap<String, Integer> category = new HashMap<>();
        ArrayList<Integer> temp = new ArrayList<>();
        
        for(int i = 0; i < terms.length; i++) {
            String[] splited = terms[i].split(" ");
            category.put(splited[0], Integer.parseInt(splited[1]));
        }
        IntegerToday[0] = Integer.parseInt(splitedToday[0]);
        IntegerToday[1] = Integer.parseInt(splitedToday[1]);
        IntegerToday[2] = Integer.parseInt(splitedToday[2]);
        
        for(int i = 0; i < privacies.length; i++) {
            String[] splitedPri = privacies[i].split(" ");  
            
            int[] curDate = convertToInt(splitedPri[0]);
            String type = splitedPri[1];
            
            curDate[1] += category.get(type);
            if(curDate[1] > 12) {
                curDate[0]+= curDate[1] % 12 == 0 ? curDate[1] /12 - 1 : curDate[1] / 12;
                curDate[1] = curDate[1] % 12 == 0 ? 12 : curDate[1] - ((curDate[1]/12) * 12);
            }
            
            if(isOver(IntegerToday, curDate)) {
                temp.add(i+1);
            }           
        }
        
        return temp.stream().mapToInt(i -> i).toArray();
    }
    
    public int[] convertToInt (String date) {
        int[] result = new int[3];
        String[] splitedDate = date.split("\\.");
        result[0] = Integer.parseInt(splitedDate[0]);
        result[1] = Integer.parseInt(splitedDate[1]);
        result[2] = Integer.parseInt(splitedDate[2]);
        return result;
    }
    
    public boolean isOver(int[] today, int[] curDay) {
        boolean isOverYear = today[0] > curDay[0];
        boolean isSameYear = today[0] == curDay[0];
        boolean isOverMonth = today[1] > curDay[1];
        boolean isSameMonth = today[1] == curDay[1];
        boolean isOverDate = today[2] >= curDay[2];
        if(isOverYear) {
            return true;
        } 
        if(isSameYear && isOverMonth) {
            return true;
        }
        if(isSameYear && isSameMonth && isOverDate) {
            return true;
        }
        return false;
    }

}