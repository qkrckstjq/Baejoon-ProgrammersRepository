import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        StringBuilder answer = new StringBuilder("");
        for(int i = 1; i < n; i++) {
            answer.append("*".repeat(i)).append("\n");
        }
        answer.append("*".repeat(n)).append("\n");
        for(int i = n - 1; i > 0; i--) {
            answer.append("*".repeat(i)).append("\n");
        }
        System.out.println(answer.toString());
    }
}