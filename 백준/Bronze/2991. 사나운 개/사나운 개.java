import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] first = br.readLine().split(" ");
        int A = Integer.parseInt(first[0]);
        int B = Integer.parseInt(first[1]);
        int C = Integer.parseInt(first[2]);
        int D = Integer.parseInt(first[3]);

        String[] second = br.readLine().split(" ");
        
        for(int i = 0; i < 3; i++) {
            int cnt = 0;
            
            int d = Integer.parseInt(second[i]);
            
            int last = d % (A + B);
            int mini = last == 0 ? d : last;
            if(mini <= A) cnt++;
            
            last = d % (C + D);
            mini = last == 0 ? d : last;
            if(mini <= C) cnt++;
            
            System.out.println(cnt);
        }
    }
}