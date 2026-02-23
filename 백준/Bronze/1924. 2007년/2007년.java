import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());

        int[] daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String[] week = {"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"};

        int total = 0;

        for (int i = 0; i < x - 1; i++) {
            total += daysInMonth[i];
        }
        total += (y - 1);

        System.out.println(week[total % 7]);
    }
}