import java.util.*;
public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] arr = sc.nextLine().split(" ");
        int a = Integer.parseInt(arr[0]);
        int b = Integer.parseInt(arr[1]);
        int n = Integer.parseInt(arr[2]) + 1;
        int temp = a % b;
        int answer= a / b;
        for(int i = 1; i < n; i++) {
            temp *= 10;
            answer = temp / b;
            temp = temp % b;
        }
        System.out.println(answer);
    } 
}