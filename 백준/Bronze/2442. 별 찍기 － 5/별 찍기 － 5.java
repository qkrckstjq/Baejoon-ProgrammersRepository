import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        StringBuilder answer = new StringBuilder("");
        
        for(int i = 1; i <= n; i++) {
            answer.append(" ".repeat(n - i));
            answer.append("*".repeat(i * 2 - 1));
            answer.append("\n");
        }
        
        System.out.println(answer);
    }
}