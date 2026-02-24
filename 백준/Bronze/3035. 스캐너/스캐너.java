import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int ZR = Integer.parseInt(st.nextToken());
        int ZC = Integer.parseInt(st.nextToken());

        StringBuilder out = new StringBuilder();

        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            StringBuilder expanded = new StringBuilder(C * ZC);

            for (int j = 0; j < C; j++) {
                char ch = line.charAt(j);
                for (int k = 0; k < ZC; k++) expanded.append(ch);
            }

            String expLine = expanded.toString();
            for (int t = 0; t < ZR; t++) out.append(expLine).append('\n');
        }

        System.out.print(out.toString());
    }
}