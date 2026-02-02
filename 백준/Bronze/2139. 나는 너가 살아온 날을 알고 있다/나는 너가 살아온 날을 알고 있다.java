import java.io.*;
import java.util.*;

public class Main {
    static boolean isLeap(int y) {
        if (y % 400 == 0) return true;
        if (y % 100 == 0) return false;
        return y % 4 == 0;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();

        int[] mdays = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        while (true) {
            String line = br.readLine();
            if (line == null) break;
            line = line.trim();
            if (line.isEmpty()) continue;

            StringTokenizer st = new StringTokenizer(line);
            int d = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            if (d == 0 && m == 0 && y == 0) break;

            int sum = d;
            for (int i = 1; i < m; i++) sum += mdays[i];
            if (m > 2 && isLeap(y)) sum += 1;

            out.append(sum).append('\n');
        }

        System.out.print(out.toString());
    }
}
