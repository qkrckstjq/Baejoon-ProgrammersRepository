import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(rd.readLine());
        long answer = 0;
        for(int i = 1; i < n; i++) {
            answer += (n * i + i);
        }
        System.out.println(answer);
    }
}