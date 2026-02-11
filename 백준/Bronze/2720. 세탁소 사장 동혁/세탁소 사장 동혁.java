import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine().trim());
        while (T-- > 0) {
            int c = Integer.parseInt(br.readLine().trim());

            int q = c / 25; c %= 25;
            int d = c / 10; c %= 10;
            int n = c / 5;  c %= 5;
            int p = c;

            sb.append(q).append(' ')
              .append(d).append(' ')
              .append(n).append(' ')
              .append(p).append('\n');
        }

        System.out.print(sb.toString());
    }
}