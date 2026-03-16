import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        for (int h = 1; h * h <= B; h++) {
            if (B % h != 0) continue;

            int w = B / h;

            if (2 * (w + h) + 4 == R) {
                System.out.println((w + 2) + " " + (h + 2));
                return;
            }
        }
    }
}