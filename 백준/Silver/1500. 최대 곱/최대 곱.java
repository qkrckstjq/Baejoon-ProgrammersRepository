import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        
        long s = Long.parseLong(input[0]);
        int k = Integer.parseInt(input[1]);
        
        long q = s / k;
        long r = s % k;
        
        long answer = 1;
        for(int i = 0; i < k; i++) {
            if(r > 0) {
                answer *= (q + 1);
                r--;
            } else {
                answer *= q;
            }
        }
        System.out.println(answer);
    }
}