import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        String[] arr = new String[n];

        for (int i = 0; i < n; i++) {
            arr[i] = rd.readLine();
        }

        Arrays.sort(arr);

        int count = n;

        for (int i = 0; i < n - 1; i++) {
            if (arr[i + 1].startsWith(arr[i])) {
                count--;
            }
        }

        System.out.println(count);
    }
}