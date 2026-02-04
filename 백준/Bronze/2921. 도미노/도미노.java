import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine().trim());

        long a = n;
        long b = n + 1;
        long c = n + 2;

        if (a % 2 == 0) a /= 2;
        else b /= 2;

        long ans = a * b * c;
        System.out.print(ans);
    }
}
