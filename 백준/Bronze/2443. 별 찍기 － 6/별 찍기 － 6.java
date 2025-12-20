import java.io.*;
class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        StringBuilder answer = new StringBuilder("");
        for(int i = n; i > 0; i--) {
            answer.append(" ".repeat(n - i));
            answer.append("*".repeat(i * 2 - 1));
            answer.append("\n");
        }
        System.out.println(answer.toString());
    }
}