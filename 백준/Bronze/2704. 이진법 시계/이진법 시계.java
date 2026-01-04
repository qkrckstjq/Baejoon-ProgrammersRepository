import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(rd.readLine());
        
        for(int i = 0; i < t; i++) {
            String[] temp = toBi(rd.readLine());
            System.out.println(temp[0] + " " + temp[1]);
        }
    }
    
    public static String[] toBi(String time) {
        String[] sp = time.split(":");
        int[] h = new int[6];
        int[] m = new int[6];
        int[] s = new int[6];
        
        String[] answer = new String[2];

        
        for(int i = 0; i < 3; i++) {
            int num = Integer.parseInt(sp[i]);
            int[] target = (i == 0) ? h : (i == 1) ? m : s;

            
            for(int j = 0; j < 6; j++) {
                int bitPos = 5 - j;
                target[j] = ((num & (1 << bitPos)) != 0) ? 1 : 0;
            }
        }

       
        StringBuilder col = new StringBuilder(18);
        for(int i = 0; i < 6; i++) {
            col.append(h[i]).append(m[i]).append(s[i]);
        }

       
        StringBuilder row = new StringBuilder(18);
        for(int i = 0; i < 6; i++) row.append(h[i]);
        for(int i = 0; i < 6; i++) row.append(m[i]);
        for(int i = 0; i < 6; i++) row.append(s[i]);

        answer[0] = col.toString();
        answer[1] = row.toString();
        return answer;
    }
}
