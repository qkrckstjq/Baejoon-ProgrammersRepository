import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int[] a = new int[9];
        int sum = 0;
        for (int i = 0; i < 9; i++) {
            a[i] = Integer.parseInt(rd.readLine());
            sum += a[i];
        }

        Arrays.sort(a);

        int target = sum - 100;
        int l = 0, r = 8;
        while (l < r) {
            int s = a[l] + a[r];
            if (s == target) break;
            if (s < target) l++;
            else r--;
        }

        for (int i = 0; i < 9; i++) {
            if (i == l || i == r) continue;
            System.out.println(a[i]);
        }
    }
}