import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) sb.append(i);

        String target = String.valueOf(n);
        System.out.println(sb.indexOf(target) + 1);
    }
}
