import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        for(int i = 0; i < N; i++) {
            String line = "";
            for(int j = 0; j < i; j++) {
                line += " ";
            }
            for(int k = i; k < N; k++) {
                line += "*";
            }
            System.out.println(line);
        }
    }
}