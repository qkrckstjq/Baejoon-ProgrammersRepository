import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));

        int[] list = new int[9];
        int sum = 0;
        for (int i = 0; i < 9; i++) {
            int num = Integer.parseInt(rd.readLine());
            list[i] = num;
            sum += num;
        }

        Arrays.sort(list);

        int target = sum - 100;
        int start = 0;
        int end = 8;

        while (start < end) {
            int temp = list[start] + list[end];
            if (target == temp) {
                break;
            } else if (target > temp){
                start++;
            } else {
                end--;
            }
        }

        for (int i = 0; i < 9; i++) {
            if(i == start || i == end) continue;
            System.out.println(list[i]);
        }
    }
}