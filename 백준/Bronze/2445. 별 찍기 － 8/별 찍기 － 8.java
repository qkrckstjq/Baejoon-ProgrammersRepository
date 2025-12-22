import java.io.*;
class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(rd.readLine());
        StringBuilder answer = new StringBuilder("");
        for(int i = 1; i <= n; i++) {
            answer.append("*".repeat(i)).append(" ".repeat(n - i));
            answer.append(" ".repeat(n - i)).append("*".repeat(i)).append("\n");
        }
        for(int i = n - 1; i >= 1; i--) {
            answer.append("*".repeat(i)).append(" ".repeat(n - i));
            answer.append(" ".repeat(n - i)).append("*".repeat(i)).append("\n");
        }
        
        wr.write(answer.toString());
        wr.flush();
    }
}