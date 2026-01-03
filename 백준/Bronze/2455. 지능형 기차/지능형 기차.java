import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {        
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int answer = 0;
        int cur = 0;
        for(int i = 0; i < 4; i++) {
            String[] input = rd.readLine().split(" ");
            int out = Integer.parseInt(input[0]);
            int in = Integer.parseInt(input[1]);
            cur = cur - out + in;
            answer = Math.max(answer, cur);
        }
        System.out.println(answer);
    }
}