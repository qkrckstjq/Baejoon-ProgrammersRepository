import java.io.*;
import java.util.*;

public class Main {
    static boolean hasDigit(int x, int d) {
        while (x > 0) {
            if (x % 10 == d) return true;
            x /= 10;
        }
        return false;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        int count = 0;
        int num = 0;

        while (count < N) {
            num++;
            if (!hasDigit(num, L)) count++;
        }

        System.out.println(num);
    }
}
