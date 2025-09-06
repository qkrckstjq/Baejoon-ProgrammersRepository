import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        StringBuilder answer = new StringBuilder("");
        for(int i = 0; i < a.length(); i++){
            char c = a.charAt(i);
            if(97 <= c && c <= 122) {
                answer.append((char) (c - 32));
            } else {
                answer.append((char) (c + 32));
            }
        }
        System.out.println(answer);
    }
}