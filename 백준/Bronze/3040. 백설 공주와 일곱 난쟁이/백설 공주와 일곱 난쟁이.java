import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] arr = new int[9];
        int sum = 0;

        for (int i = 0; i < 9; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            sum += arr[i];
        }

        int target = sum - 100;
        int first = -1;
        int second = -1;

        for (int i = 0; i < 8; i++) {
            for (int j = i + 1; j < 9; j++) {
                if (arr[i] + arr[j] == target) {
                    first = i;
                    second = j;
                    break;
                }
            }
            if (first != -1) {
                break;
            }
        }

        for (int i = 0; i < 9; i++) {
            if (i == first || i == second) {
                continue;
            }
            System.out.println(arr[i]);
        }
    }
}