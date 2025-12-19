import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long N = Long.parseLong(br.readLine().trim());

        int k = 1;
        int sec = 0;

        while (N > 0) {
            if (N >= k) {
                N -= k;
                k++;
                sec++;
            } else {
                k = 1;
            }
        }

        System.out.println(sec);
    }
}