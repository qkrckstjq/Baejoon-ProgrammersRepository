import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(rd.readLine());
        while(0 < T--) {
            String temp = rd.readLine();
            String[] sb = rd.readLine().split(" ");
            String[] sList = rd.readLine().split(" ");
            String[] bList = rd.readLine().split(" ");
            int s = 0;
            int b = 0;
            for(String num : sList) {
                s = Math.max(Integer.parseInt(num), s);
            }
            for(String num : bList) {
                b = Math.max(Integer.parseInt(num), b);
            }
            
            if(s >= b) {
                System.out.println("S");
            } else {
                System.out.println("B");
            }
        }
    }
}