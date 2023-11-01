import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int [photo.length];
        HashMap<String, Integer> dataObj = makeObject(name, yearning);
        for(int i = 0; i < photo.length; i++) {
            int temp = 0;
            for(int j = 0; j < photo[i].length; j++) {
                Integer value = dataObj.get(photo[i][j]);
                if(value != null) {
                    temp+=value;
                }
            }
            answer[i] = temp;
        }
        
        return answer;
    }
    
    public static HashMap<String, Integer> makeObject(String[] names, int[] yearning) {
        HashMap<String, Integer> object = new HashMap<>();
        for(int i = 0; i < names.length; i++) {
            object.put(names[i], yearning[i]);
        }
        return object;
    }
}

