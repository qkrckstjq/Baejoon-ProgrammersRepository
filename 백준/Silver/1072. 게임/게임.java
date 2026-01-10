import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(rd.readLine());

        long t = Long.parseLong(st.nextToken());
        long v = Long.parseLong(st.nextToken());

        long z = (v * 100) / t;                
        if (z >= 99) {                         
            System.out.println(-1);
            return;
        }

        long lo = 1;
        long hi = 1_000_000_000L;              
        long ans = -1;

        while (lo <= hi) {
            long mid = (lo + hi) >>> 1;        

            long nz = ((v + mid) * 100) / (t + mid);
            if (nz > z) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }

        System.out.println(ans);
    }
}
