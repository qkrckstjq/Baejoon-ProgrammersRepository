import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        Map<Integer, Integer> order = new HashMap<>();

        int current = N;
        int idx = 0;

        while (true) {
            current = (current * N) % P;

            if (order.containsKey(current)) {
                System.out.println(idx - order.get(current));
                break;
            }

            order.put(current, idx);
            idx++;
        }
    }
}