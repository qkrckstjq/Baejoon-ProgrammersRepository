import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringBuilder out = new StringBuilder();
        for (int tc = 0; tc < T; tc++) {
            String msg = br.readLine();
            String rule = br.readLine();

            StringBuilder sb = new StringBuilder(msg.length());
            for (int i = 0; i < msg.length(); i++) {
                char c = msg.charAt(i);
                if (c == ' ') sb.append(' ');
                else sb.append(rule.charAt(c - 'A'));
            }

            out.append(sb);
            if (tc + 1 < T) out.append('\n');
        }

        System.out.print(out.toString());
    }
}