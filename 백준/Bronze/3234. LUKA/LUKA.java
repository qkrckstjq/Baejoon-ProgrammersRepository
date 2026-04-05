import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int X = Integer.parseInt(st.nextToken());
        int Y = Integer.parseInt(st.nextToken());

        int K = Integer.parseInt(br.readLine());
        String route = br.readLine();

        int x = 0, y = 0;

        StringBuilder sb = new StringBuilder();
        boolean found = false;

        if (Math.abs(x - X) <= 1 && Math.abs(y - Y) <= 1) {
            sb.append(0).append('\n');
            found = true;
        }

        for (int i = 0; i < K; i++) {
            char c = route.charAt(i);

            if (c == 'I') x++;
            else if (c == 'Z') x--;
            else if (c == 'S') y++;
            else if (c == 'J') y--;

            if (Math.abs(x - X) <= 1 && Math.abs(y - Y) <= 1) {
                sb.append(i + 1).append('\n');
                found = true;
            }
        }

        if (!found) System.out.println(-1);
        else System.out.print(sb);
    }
}