import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int[] input = Arrays.stream(rd.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .sorted()
            .toArray();
        System.out.println(input[0] * input[2]);
    }
}