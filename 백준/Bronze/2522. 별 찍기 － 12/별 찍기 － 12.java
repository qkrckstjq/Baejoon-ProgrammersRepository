import java.io.*;
class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        StringBuilder answer = new StringBuilder("");
        for(int i = 0; i < n - 1; i++) {
            answer.append(" ".repeat(n - 1 - i));
            answer.append("*".repeat(i + 1));
            answer.append("\n");
        }
        answer.append("*".repeat(n));
        answer.append("\n");
        for(int i = 0; i < n - 1; i++) {
            answer.append(" ".repeat(i + 1));
            answer.append("*".repeat(n - 1 - i));
            answer.append("\n");
        }
        System.out.println(answer.toString());
    }
}