import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        long answer = 2;
        for(int i = 0; i < n; i++) {
            answer = answer + (answer - 1);
        }
        System.out.printf("%.0f", Math.pow(answer, 2));
    }
}