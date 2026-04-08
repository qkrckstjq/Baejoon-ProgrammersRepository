import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int a = n / 2;
        int b = n - a;

        System.out.println((a + 1) * (b + 1));
    }
}