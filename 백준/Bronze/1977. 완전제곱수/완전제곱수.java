import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(rd.readLine());
        int n = Integer.parseInt(rd.readLine());
        int min = 100000;
        int answer = 0;
        for(int i = 1; i <= 100; i++) {
            int temp = i * i;
            if(m <= temp && temp <= n) {
                if(min == 100000) {
                    min = temp;
                }
                answer += temp;
            }
        }
        
        if(min == 100000) {
            System.out.println(-1);
        } else {
            System.out.printf("%d\n%d",answer, min);
        }
    }    
}

