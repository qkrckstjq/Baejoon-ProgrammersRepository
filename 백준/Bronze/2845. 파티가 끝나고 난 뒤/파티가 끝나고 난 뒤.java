import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int L = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        int expected = L * P;

        st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 5; i++) {
            int x = Integer.parseInt(st.nextToken());
            sb.append(x - expected);
            if (i < 4) sb.append(' ');
        }
        System.out.print(sb.toString());
    }
}