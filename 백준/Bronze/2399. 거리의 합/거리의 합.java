import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());      // 첫 줄: n
        String[] input = sc.nextLine().split(" ");   // 둘째 줄: 좌표들

        long answer = 0L;                            // int → long
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(input[i]);
        }

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                answer += Math.abs(arr[i] - arr[j]) * 2L;  // long 연산
            }
        }

        System.out.println(answer);
    }
}