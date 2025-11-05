import java.util.*;
class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        for(int i = 1; i <= num; i++) {
            String line = "*".repeat(i);
            System.out.println(line);
        }
    }
}