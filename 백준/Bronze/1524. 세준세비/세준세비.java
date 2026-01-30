import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(rd.readLine());
        while(0 < T--) {
            String temp = rd.readLine();
            String[] sb = rd.readLine().split(" ");
            int s = Arrays.stream(rd.readLine().split(" "))
                .map(Integer::parseInt)
                .reduce(0, (result, n) -> Math.max(result, n));
            int b = Arrays.stream(rd.readLine().split(" "))
                .map(Integer::parseInt)
                .reduce(0, (result, n) -> Math.max(result, n));
            if(s >= b) {
                System.out.println("S");
            } else {
                System.out.println("B");
            }
        }
    }
}