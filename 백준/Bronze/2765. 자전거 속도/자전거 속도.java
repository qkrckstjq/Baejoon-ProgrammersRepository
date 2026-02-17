import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        int trip = 1;

        final double PI = Math.PI;
        final double INCH_PER_MILE = 12.0 * 5280.0;

        while ((line = br.readLine()) != null) {
            line = line.trim();
            if (line.isEmpty()) continue;

            StringTokenizer st = new StringTokenizer(line);
            double d = Double.parseDouble(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            double t = Double.parseDouble(st.nextToken());

            if (r == 0) break;

            double distanceMile = (PI * d * r) / INCH_PER_MILE;
            double timeHour = t / 3600.0;
            double mph = distanceMile / timeHour;

            System.out.printf(Locale.US, "Trip #%d: %.2f %.2f%n", trip, distanceMile, mph);
            trip++;
        }
    }
}