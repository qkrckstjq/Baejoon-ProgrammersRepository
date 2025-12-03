import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int L = Integer.parseInt(input[1]);
        int D = Integer.parseInt(input[2]);
        
        int[] arr = new int[N * L + (N - 1) * 5];
        for(int i = 0; i < N; i++) {
            for(int j = i * (L + 5); j < i * (L + 5) + L; j++) {
                arr[j] = 1;
            }
        }
        int t = 0;
        while(true) {
            t += 1;
            if(t * D >= arr.length || arr[t * D] == 0) {
                break;
            }
        }
        System.out.println(t * D);
    }
}