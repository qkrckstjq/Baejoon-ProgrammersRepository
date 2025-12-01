import java.util.*;
class Main {
    public static void main(String[] args) {
        int answer = 0;
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int start = Integer.parseInt(input[0]);
        int end = Integer.parseInt(input[1]);
        int c = 1;
        for(int i = 1; i <= end; i++) {
            for(int j = 0; j < i; j++) {
                if(start <= c && c <= end) {
                    answer += i;
                }
                c++;
            }
        }
        System.out.println(answer);
    }
}