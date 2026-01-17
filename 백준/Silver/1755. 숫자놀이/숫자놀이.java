import java.io.*;
import java.util.*;

class Main {
    public static Map<Character, String> map = new HashMap<>();
    
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] input = rd.readLine().split(" ");
        int start = Integer.parseInt(input[0]);
        int end = Integer.parseInt(input[1]);
        map.put('0', "zero");
        map.put('1', "one");
        map.put('2', "two");
        map.put('3', "three");
        map.put('4', "four");
        map.put('5', "five");
        map.put('6', "six");
        map.put('7', "seven");
        map.put('8', "eight");
        map.put('9', "nine");
        
        List<Integer> list = new ArrayList<>();
        for(int i = start; i <= end; i++) {
            list.add(i);
        }
        
        list.sort(Comparator.comparing(Main::numToStr));
            
        
        StringBuilder answer = new StringBuilder("");
        for(int i = 0; i < list.size(); i+= 10) {
            for(int j = i; j < Math.min(list.size(), i + 10); j++) {
                answer.append(Integer.toString(list.get(j)) + " ");
            }
            answer.append("\n");
        }
        System.out.println(answer.toString());
    }
    
    public static String numToStr(int num) {
        StringBuilder result = new StringBuilder("");
        String str = Integer.toString(num);
        for(int i = 0; i < str.length(); i++) {
            result.append(map.get(str.charAt(i)) + " ");
        }
        return result.toString();
    }
}