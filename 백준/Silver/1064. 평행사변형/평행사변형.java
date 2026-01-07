import java.io.*;
import java.util.*;

public class Main {
    static double dist(long x1, long y1, long x2, long y2) {
        long dx = x1 - x2;
        long dy = y1 - y2;
        return Math.sqrt((double)dx * dx + (double)dy * dy);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long x1 = Long.parseLong(st.nextToken());
        long y1 = Long.parseLong(st.nextToken());
        long x2 = Long.parseLong(st.nextToken());
        long y2 = Long.parseLong(st.nextToken());
        long x3 = Long.parseLong(st.nextToken());
        long y3 = Long.parseLong(st.nextToken());
        long cross = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1);
        if (cross == 0) {
            System.out.println(-1);
            return;
        }

        double ab = dist(x1, y1, x2, y2);
        double ac = dist(x1, y1, x3, y3);
        double bc = dist(x2, y2, x3, y3);

        double p1 = 2.0 * (ab + ac);
        double p2 = 2.0 * (ab + bc);
        double p3 = 2.0 * (ac + bc);

        double maxP = Math.max(p1, Math.max(p2, p3));
        double minP = Math.min(p1, Math.min(p2, p3));

        double ans = maxP - minP;
        System.out.printf("%.10f%n", ans);
    }
}