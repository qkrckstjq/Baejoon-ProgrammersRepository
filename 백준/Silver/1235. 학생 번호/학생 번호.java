import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        String[] input = new String[n];
        for(int i = 0; i < n; i++) {
            input[i] = rd.readLine();
        }
        
        int answer = 0;
        int len = input[0].length();
        for(int i = 1; i <= len; i++) {
            Set<String> dup = new HashSet<>();
            boolean d = false;
            for(int j = 0; j < n; j++) {
                String temp = input[j].substring(len - i, len);
                if(dup.contains(temp)) {
                    d = true;
                    break;  
                }
                dup.add(temp);
            }
            if(!d) {
                answer = i;
                break;
            }
            dup = new HashSet<>();
        }
        System.out.println(answer);
    }
}