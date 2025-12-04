import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        int s = 0;
        int e = input.length() - 1;
        for(int i = 0; i < input.length() - 1; i++) {
            String left = "";
            String right = "";
            for(int q = s; q <= i; q++) {
                left += input.charAt(q);
            }
            for(int r = e; r > i; r--) {
                right += input.charAt(r);
            }
            if(getM(left) == getM(right)) {
                System.out.println("YES");
                return;
            }
        }
        System.out.println("NO");
    }
    
    public static int getM(String num) {
        int result = 1;
        for(int i = 0; i < num.length(); i++) {
            result *= (num.charAt(i) - '0');
        }
        return result;
    }
}