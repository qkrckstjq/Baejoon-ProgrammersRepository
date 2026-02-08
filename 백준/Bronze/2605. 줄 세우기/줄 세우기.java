import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        StringTokenizer st = new StringTokenizer(br.readLine());

        List<Integer> line = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            int x = Integer.parseInt(st.nextToken());
            int pos = line.size() - x;
            line.add(pos, i);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < line.size(); i++) {
            if (i > 0) sb.append(' ');
            sb.append(line.get(i));
        }
        System.out.print(sb.toString());
    }
}