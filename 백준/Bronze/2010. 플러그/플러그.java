import java.io.*;
class Main {
    public static void main (String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        int answer = 0;
        for(int i = 0; i < n; i++) {
            answer += Integer.parseInt(rd.readLine());
        }
        System.out.println(answer - (n - 1));
    }
}