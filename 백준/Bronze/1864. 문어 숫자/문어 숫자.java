import java.io.*;
import java.util.*;
class Main {
    public static void main(String[] args) throws Exception {
        Map<String, Integer> map = new HashMap<>();
        map.put("-", 0);
        map.put("\\", 1);
        map.put("(", 2);
        map.put("@", 3);
        map.put("?", 4);
        map.put(">", 5);
        map.put("&", 6);
        map.put("%", 7);
        map.put("/", -1);
        
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String line = "";
        while(true) {
            line = rd.readLine();
            if(line.equals("#")) break;
            System.out.println(getNum(line, map));
        }
        return;
    }
    public static int getNum(String num, Map<String, Integer> map) {
        int answer = 0;
        for(int i = 0; i < num.length(); i++) {
            answer += (Math.pow(8, num.length() - (i + 1)) * map.get(Character.toString(num.charAt(i))));
        }
        return answer;
    }
}