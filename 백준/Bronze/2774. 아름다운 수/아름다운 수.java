import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(rd.readLine());
        while(0 < t--) {
            int[] set = new int[11];
            String input = rd.readLine();
            for(int i = 0; i < input.length(); i++) {
                int num = input.charAt(i) - '0';
                set[num] += 1;
            }
            int result = 0;
            for(int i = 0; i <= 10; i++) {
                if(set[i] != 0) result += 1;
            }
            System.out.println(result);
        }
    }
}