import java.util.*;
import java.io.*;
class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(reader.readLine());
        StringBuilder answer = new StringBuilder("");
        for(int i = 0; i < N; i++) {
            answer.append("*".repeat(N - i));
            answer.append("\n");
        }
        System.out.println(answer.toString());
    }
}