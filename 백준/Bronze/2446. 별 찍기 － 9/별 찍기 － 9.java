import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        StringBuilder answer = new StringBuilder("");
        for(int i = n; i > 0; i--) {
            answer.append(" ".repeat(n - i)).append("*".repeat(i * 2 - 1)).append("\n");
        }
        for(int i = 2; i <= n; i++) {
            answer.append(" ".repeat(n - i)).append("*".repeat(i * 2 - 1)).append("\n");
        }
        System.out.println(answer.toString());
    }
}